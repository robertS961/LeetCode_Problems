class Solution(object):
    def countOfAtoms(self, formula):
        import re
        from collections import defaultdict
        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        stack, i = [defaultdict(int)], 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(defaultdict(int))
            else:
                count = 1
                # Check if next token is a number.
                if i + 1 < len(tokens) and re.search('^\d+$', tokens[i + 1]):
                    count, i = int(tokens[i + 1]), i + 1
                atoms = stack.pop() if token == ')' else { token: 1 }
                # Combine counts of atoms.
                for atom in atoms:
                    stack[-1][atom] += atoms[atom] * count
            i += 1
        return ''.join([atom + (str(count) if count > 1 else '') for atom, count in sorted(stack[-1].items())])