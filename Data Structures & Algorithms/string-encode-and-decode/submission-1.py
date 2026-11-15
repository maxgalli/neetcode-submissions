class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "oidocrop"
        return "porcodio".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "oidocrop":
            return []
        return s.split("porcodio")