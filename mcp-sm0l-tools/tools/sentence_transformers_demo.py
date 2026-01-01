from __future__ import annotations

try:
    from sentence_transformers import SentenceTransformer, util
except ImportError:
    print("Missing dependency: sentence-transformers. Install with: pip install sentence-transformers")
    raise SystemExit(0)

if __name__ == "__main__":
    model = SentenceTransformer("all-MiniLM-L6-v2")
    s = ["the cat sits", "a dog runs", "cats are animals"]
    emb = model.encode(s, normalize_embeddings=True)
    sims = util.cos_sim(emb[0], emb).tolist()[0]
    print(list(zip(s, [round(x,3) for x in sims])))
