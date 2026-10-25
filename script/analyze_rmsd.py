import os
import sys
import numpy as np
from Bio.PDB import PDBParser, Superimposer

def calculate_ca_rmsd(wt_pdb_path: str, mut_pdb_path: str):
    """
    Parses two PDB structures, extracts alpha-carbon (C-alpha) coordinates,
    superimposes them using the Kabsch algorithm, and prints the overall RMSD.
    """
    if not os.path.exists(wt_pdb_path) or not os.path.exists(mut_pdb_path):
        print(f"Error: One or both coordinate files not found.\n  WT: {wt_pdb_path}\n  MUT: {mut_pdb_path}")
        sys.exit(1)

    parser = PDBParser(QUIET=True)
    
    # Load structures
    struct_wt = parser.get_structure("WT", wt_pdb_path)
    struct_mut = parser.get_structure("MUT", mut_pdb_path)

    # Extract first model of each (AlphaFold output standard)
    model_wt = struct_wt[0]
    model_mut = struct_mut[0]

    # Collect C-alpha atoms for mature catalytic domain (skipping flexible signal peptide 1-23)
    ca_atoms_wt = [atom for atom in model_wt.get_atoms() if atom.get_name() == 'CA' and atom.get_parent().id[1] > 23]
    ca_atoms_mut = [atom for atom in model_mut.get_atoms() if atom.get_name() == 'CA' and atom.get_parent().id[1] > 23]

    if len(ca_atoms_wt) != len(ca_atoms_mut):
        print(f"Atom count mismatch: WT has {len(ca_atoms_wt)} C-alphas, MUT has {len(ca_atoms_mut)} C-alphas.")
        sys.exit(1)

    # Superimpose using SVD (Kabsch algorithm)
    super_imposer = Superimposer()
    super_imposer.set_atoms(ca_atoms_wt, ca_atoms_mut)
    super_imposer.apply(model_mut.get_atoms())

    rmsd = super_imposer.rms
    print("=" * 45)
    print("  TEM-1 STRUCTURAL SUPERPOSITION ANALYSIS  ")
    print("=" * 45)
    print(f"Aligned C-alpha pairs (residues 24-286): {len(ca_atoms_wt)}")
    print(f"C-alpha Backbone RMSD: {rmsd:.4f} Å")
    print("=" * 45)

    if rmsd < 0.5:
        print("Verdict: Fold completely conserved (no structural collapse).")
    else:
        print("Verdict: Measurable backbone conformational shift observed.")

if __name__ == "__main__":
    # Update paths if your files are in a structures/ subfolder
    calculate_ca_rmsd("wt.pdb", "mut.pdb")