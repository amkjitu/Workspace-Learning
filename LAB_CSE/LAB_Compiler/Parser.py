from parse_tree import Node


def Parser(CFG, input):
    print("\nProvided contex-free grammar:")
    print(CFG)
    print("\nProvided input string:", input)
    rules = CFG['S']

    if CFG != {}:
        out, parse_tree, match, input_iter = rec_parse(
            CFG, "S", input, 0, "", Node("S"), [], 0)
        print("\n\nEnd of input parsing")
        if match == True and (out == input or out == input[:-1]) and parse_tree != []:
            print("Input string accepted by the CFG\n")
            print_parse_tree(parse_tree)
        else:
            print("Input string not accepted by the CFG.\n")


def rec_parse(CFG, nonterminal, input, input_iter, out, node, parse_tree, matched):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)

    parse_tree.append(node)

    for rule in rules:
        match = False
        matched = 0
        for i in range(len(rule)):
            node.add_children(rule[i])
            print_parse_tree(parse_tree)

            print("Current production rule {} : {}".format(nonterminal, rule))
            print("Current input character " + input[input_iter])
            if rule[i].isupper() == True:
                out, parse_tree, match, input_iter = rec_parse(
                    CFG, rule[i], input, input_iter, out, Node(rule[i]), parse_tree, matched)
                if out == input[:-1] and match == True:
                    match = True
                    return out, parse_tree, match, input_iter
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1
                    matched += 1
                    match = True
                elif rule[i] == '$':
                    match = True
                    continue
                else:
                    print("\t\tBacktracking...")
                    for el in range(matched):
                        out = out.replace(out[el], "")
                        input_iter = input_iter - 1

                    node.remove_children()
                    match = False
                    matched = 0
                    break

        if (out == input[:-1] or out == input or input == '$') and match == True:
            match = True
            return out, parse_tree, match, input_iter

        if (out == input[:-1] or out == input or input == '$') and match == True:
            return out, parse_tree, match, input_iter

    return out, parse_tree, match, input_iter


def print_parse_tree(parse_tree):
    for el in parse_tree:
        if el.children == []:
            parse_tree.remove(el)

    if len(parse_tree) == 0:
        return

    print("\n-------------------------    PARSE TREE      -------------------------")
    for el in parse_tree:
        el.print_node()
    print("----------------------------------------------------------------------\n")
