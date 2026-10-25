# Structural Characterization of TEM-1 $\beta$-Lactamase Catalytic Inactivation

## Overview
This repository provides an in silico structural comparison between wild-type TEM-1 $\beta$-lactamase (*Escherichia coli*) and its catalytic active-site mutant. TEM-1 confers resistance against $\beta$-lactam antibiotics by hydrolyzing the four-membered $\beta$-lactam ring. 

Here, structural models were generated using **AlphaFold2**, superimposed, and quantitatively analyzed using **BioPython** and **PyMOL** to evaluate whether functional inactivation stems from global structural destabilization or localized chemical modification.

---

## Computational Methodology
1. **Sequence Retrieval:** Canonical wild-type sequence fetched from UniProt (`P62593`).
2. **Structural Prediction:** AlphaFold2 via ColabFold (MMseqs2 MSA homology engine; 3 recycles).
3. **Superposition & RMSD Calculation:** Automated Python pipeline using `Bio.PDB.Superimposer` (Singular Value Decomposition / Kabsch algorithm).
4. **Visualization:** PyMOL open-source ray-tracing engine.

---

## Quantitative Results

Backbone superposition of the mature catalytic domain (residues 24–286, excluding the N-terminal signal peptide) was executed across all $C_\alpha$ pairs:

| Metric | Measured Value | Biological Interpretation |
| :--- | :--- | :--- |
| **Aligned $C_\alpha$ Pairs** | 263 | Full mature catalytic core |
| **Backbone RMSD** | **0.0586 Å** | Global fold strictly conserved |
| **Mechanism** | Catalytic Knockout | Local nucleophile loss without structural collapse |

### Execution Log
```text
=============================================
  TEM-1 STRUCTURAL SUPERPOSITION ANALYSIS  
=============================================
Aligned C-alpha pairs (residues 24-286): 263
C-alpha Backbone RMSD: 0.0586 Å
=============================================
Verdict: Fold completely conserved (no structural collapse).