# Structural Analysis of TEM-1 $\beta$-Lactamase Catalytic Inactivation

## Project Overview
This repository investigates the structural mechanism of catalytic inactivation in TEM-1 $\beta$-lactamase (*Escherichia coli*). TEM-1 confers resistance to $\beta$-lactam antibiotics by hydrolyzing the strained four-membered $\beta$-lactam ring. 

In this computational project, 3D structural models of wild-type TEM-1 (UniProt: P62593) and its active-site mutant (Ser $\rightarrow$ Ala) were generated using **AlphaFold2 (via ColabFold)**, aligned in **PyMOL**, and analyzed using **BioPython**.

## Active-Site Superposition
Below is the structural overlay of the wild-type active site (marine blue) against the alanine mutant (salmon pink).

![Active Site Overlay](figures/active_site_overlay.png)

## Findings
1. **Global Fold Stability:** Backbone superposition yielded an Alpha-Carbon RMSD < 0.4 Å, demonstrating that the single-point substitution causes no global structural collapse.
2. **Loss of Catalytic Nucleophile:** Wild-type Serine presents a nucleophilic hydroxyl group (-OH) oriented toward Lysine for proton abstraction and antibiotic ring attack. The alanine mutant truncates this side chain to an inert methyl group (-CH3), physically eliminating the reactive nucleophile required for $\beta$-lactam ring hydrolysis.

## Methodology
* **Prediction:** AlphaFold2 via ColabFold (MMseqs2 homology search).
* **Superposition & Visualization:** PyMOL open-source.
* **RMSD Analysis:** BioPython (`Bio.PDB.Superimposer`).