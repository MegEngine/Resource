import megengine as mge
import megengine.functional as F
import megengine.module as M


class PatchEmbed(M.Module):
    def __init__(self, img_size=(224, 224), patch_size=(16, 16), in_chans=3, embed_dim=768):
        super().__init__()
        self.embed_dim = embed_dim
        self.img_size = img_size
        self.grid_size = (img_size[0] // patch_size[0], img_size[1] // patch_size[1])
        self.num_patches = self.grid_size[0] * self.grid_size[1]
        self.proj = M.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x):
        B, C, H, W = x.shape
        assert (H, W) == self.img_size
        x = self.proj(x)
        x = x.reshape(B, self.embed_dim, self.num_patches).transpose(0, 2, 1)  # BCHW -> BNC
        return x


class MLP(M.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None, bias=True):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features

        self.fc1 = M.Linear(in_features, hidden_features, bias=bias)
        self.act = M.GELU()
        self.fc2 = M.Linear(hidden_features, out_features, bias=bias)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.fc2(x)
        return x


class MixerBlock(M.Module):
    def __init__(self, dim, seq_len, mlp_ratio=(0.5, 4.0)):
        super().__init__()
        tokens_dim, channels_dim = [int(x * dim) for x in mlp_ratio]
        self.norm1 = M.LayerNorm(dim, eps=1e-6)
        self.mlp_tokens = MLP(seq_len, tokens_dim)
        self.norm2 = M.LayerNorm(dim, eps=1e-6)
        self.mlp_channels = MLP(dim, channels_dim)

    def forward(self, x):
        x = x + self.mlp_tokens(self.norm1(x).transpose(0, 2, 1)).transpose(0, 2, 1)
        x = x + self.mlp_channels(self.norm2(x))
        return x


class MLPMixer(M.Module):
    def __init__(
            self,
            num_classes=1000,
            img_size=(224, 224),
            in_chans=3,
            patch_size=(16, 16),
            num_blocks=8,
            embed_dim=512,
            mlp_ratio=(0.5, 4.0),
    ):
        super().__init__()
        self.stem = PatchEmbed(img_size=img_size, patch_size=patch_size, in_chans=in_chans, embed_dim=embed_dim)
        self.blocks = M.Sequential(*[
            MixerBlock(embed_dim, self.stem.num_patches, mlp_ratio)
            for _ in range(num_blocks)
        ])
        self.norm = M.LayerNorm(embed_dim, eps=1e-6)
        self.head = M.Linear(embed_dim, num_classes) if num_classes > 0 else M.Identity()

    def forward_features(self, x):
        x = self.stem(x)
        x = self.blocks(x)
        x = self.norm(x)
        return x

    def forward(self, x):
        x = self.forward_features(x)
        x = x.mean(1)
        x = self.head(x)
        return x

    def load_from_torch(self, torch_state_dict):
        sd = {k: v.numpy() for k, v in torch_state_dict.items()}
        sd['stem.proj.bias'] = sd['stem.proj.bias'].reshape(1, -1, 1, 1)
        self.load_state_dict(sd)


# 请将下面的 URL 替换为提交权重文件后得到的 URL
@mge.hub.pretrained('http://localhost:8000/mlp_mixer_b16_224.pkl')
def mlp_mixer_b16_224():
    return MLPMixer(num_blocks=12, embed_dim=768)
