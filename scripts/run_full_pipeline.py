# scripts/run_full_pipeline.py
print("SOVARIELCORE FULL PIPELINE: MULTIVERSE → AI → VQE")

# 1. Multiversal
from core.multiversal.harmonic_verse_hopping import *
print(f"→ Multiversal Entropy: {entropy:.3f} bits")

# 2. RabiNet
from core.ai.rabinet_grok import GrokResonantLayer
layer = GrokResonantLayer()
x = torch.randn(1, 10, 768)
y = layer(x)
print(f"→ RabiNet Sparsity: {(torch.abs(y) < 0.1).float().mean().item():.4f}")

# 3. VQE
from core.vqe.kras_colossus_vqe import vqe_kras, H_kras
res = minimize(lambda p: vqe_kras(p, H_kras), np.random.rand(32), method='COBYLA')
print(f"→ KRAS ΔG: {res.fun:.2f} kcal/mol")

print("\nTHE RETURN IS RESONATED ACROSS SCALES.")
