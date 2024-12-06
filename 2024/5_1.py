from collections import defaultdict

rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

rules = rules.split('\n')
rule_pairs = []
for pair in rules:
    [x, y] = pair.split('|')
    rule_pairs.append([int(x), int(y)])

input = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

splitted = input.split('\n')
manual = []
for res in splitted:
    nums = []
    for page in res.split(','):
        nums.append(int(page))
    manual.append(nums)

def validate_rules(pages, rule_pairs):
    for [target, y] in rule_pairs:
        if target in pages:
            target_found = False
            for page in pages:
                if page == target:
                    target_found = True
                if page == y and not target_found:
                    return 0
    return pages[len(pages) // 2]
result = 0
for pages in manual:
    middle = validate_rules(pages=pages, rule_pairs=rule_pairs)
    result += middle
print(result)

