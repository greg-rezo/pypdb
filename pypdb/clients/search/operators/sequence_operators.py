"""Search operator for searching sequences using MMseqs2 (BLAST-like)."""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Union

class SequenceType(Enum):
    """Type of sequence being searched."""
    DNA = "pdb_dna_sequence"
    RNA = "pdb_rna_sequence"
    PROTEIN= "pdb_protein_sequence"


@dataclass
class SequenceOperator:
    """Default search operator; searches across available fields search,
    and returns a hit if a match happens in any field."""
    sequence: str
    sequence_type: SequenceType
    # Maximum E Value allowed for results
    # (see: https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html)
    evalue_cutoff: float = 100
    # Minimum identity cutoff allowed for results
    # (see: https://www.ncbi.nlm.nih.gov/books/NBK62051/def-item/identity/)
    identity_cutoff: float = 0.95

    def _to_dict(self) -> Dict[str, Any]:
        return {
            "evalue_cutoff": self.evalue_cutoff,
            "identity_cutoff": self.identity_cutoff,
            "target": self.sequence_type.value,
            "value": self.sequence
        }
