import quadgram_scorer
import random

ciphertext = "LBAGFUWXZHRKIYZIQLEWNVUDXHIVMGGBVUVIEWINBZCPNHIKXWKCNUEWKCMGCAWHWZBLHUAGDVYKHYYCGUIFUHXIHUKOOPFXURHLWXNSEWMIEWPOGZTAXNZOLZOKMPBCIHGZIYZHOKGUITMIEWALTYYGGVIKZNHVMLRGGBVIGOEWYGLAHYCXIGWXKLGZIYZHYIIKUHAGDVYKBLKLEWQGTIIPXWBGQLEWVNMLPAGZTYBHQDLAXNHUCYLFIOKCYHMDLBIKUWLADQIKZNKCCGVUWHYBOKHVYGLMHUWXMIOPIKZNEWCHYCBGIUYMZTGHXHTYYKIKKOWXVNXNOGAGNVLUTYBGNVIEUHWHZHKLEWOGYLQLEWLCZHGMTYXHTYYKHYNGGQHONGKYYBAGDVYKIKXIHUKOHYMGUHHLFOXNGOIEDPYALZWXVHNVIKZNIGTAXNCOHOHNHWZVAPYRKLLBIKUHGZTYAGDVYKHYMGEWDHTYYKWXWNDIYIIYXHTYYKYGALIKAZQCXNAGDVYKIEUHZHHUAYELKYVZUHNBEWHUAGDVYKHYFQUHXNIKVZGTHXAGDVYKFZGVOGIKVUZNXWLBAGDVYTMYLAOKGFOHNTMEGWOWIUYGOTINGUIPIBWXKOYDWXPLFRIYYDIKALHWAGDVYKIKKOAYVPZAAGMEUHWXINIKNVYGOTMPVUXNAGDVYKIKVZGTHXWXVNXNLEQGIKWHOGAGNVQGHCTLKILUTYIKVIKHIYWNGQUIWFGOEWNBROHVMGIBCHNGOKMPQGGZGYNHCHIBIETIXNLAGOANBCGNIWKCZVAGNVOGRGHOYTFURUTYGWXHTYYKGZYBYGIQKCLMALNTWXCBHVYGXYGOAYFRALNTWXMGGBWHPYZWCRVMTAHYBCFQEWMIEWINRAXNINGKEICBNXQGALNZCXTYYKBCGNIKXILHGPGOHYPDLZRUTYGWXNOGLTZVNVFAHODWAGDVYKBCGNIKXWRCHURHIBYGOKMPAYFRALNTWXMGGLTEVNZHEWCHGKTYYKBCGNIKVINHBIGYYKMPGOHYPDLZRUTYGWXNOGLTZVNVAGFUCOXHTYYKBCGNIKXHIBCHPGPOTGMPGOGWIKWIGHHVNSTORKHUROOPNXQGALNZYCQCXNIKVZGTHXAGDVYKHYCSYGALIKMOAIXLKITOLKVNFOXNROTOOIXNGONZGXTYYKWCZHDWIWHUCXTYYKTNUIIVNCUHINIKZOXRHVOGWQKOUHYGGMZHKPXHTYYKBCGNIKVZGTHXAGDVYKAIQFXPNXHIUIGRTYYKAGNVOGNVOGYTCUALSHTYYKBLHLPVQGKCZVOTNVOGIKNHHTOGZVCPGOAYEZWECYRPWHOMLBOTNVROHUCYDATYYKBCGNIKVINHBIGYYKYHDIHLOPYGIQXWKCMIBHTOCYZAIGDIUHAGDVYKBCGNIKXWRCHURHIBYGOMLZPVQGHVUNAYFURUTYGWXWOGXFVURGHONVCSYGALIKDPGOIKUITGMIAIXLKITONTICOQZHFQUIIOLBHLICIVMIEWINBZCPAGDVYKBGEWOCZVROCHIXAGDVYKIGXPALCHAGDVYKIEGHEICBBGWLUHHXHYCSPCZHPSFPIKKOOGOGLEYNXNHBZALUTYENNTYHORKPHYMGLNNUYGZVKLEWGXHUWHIKKOQGGZGYNHCRLAHWCPGOCBTOWUGUIFTOKCRHCBKIEWPOGZTAXNIKKOBHDATYYKHYMGEWHWVGYTNVMIROIGQLEWNQUHUWTIIUNSTOEIIYNXCPGOBLKLEWDBHBAGDVYKQGHYNGDINHLEQGIKXWYLGVIKXWRHVUWHKCNCGNNXDHTYYKROTOOIZIGPYKDHTYYKINIKZORONCZHYCMPHBHLMHIUPSCRXHTYYKIEGBVUVNXNOGWZCBPVRKFXURHLWXYCQGEWNBUHXNGOIKVINHBIGYYKDHTYYKHCGWNHICGWCZXHTYYKUFWCXNOGBHCPIKUITOOIVNHYHYCXHLXNLZGKTYYKIEYZHUAYELKYYBAGDVYKIKXIHUKOHYMGUHHLFOXHTYYKBCGNIKUITOOIVNHYAGDVYKNHKOHUYQITDIZTGHXNGOFZGMIYGQLKTHVNUNIUCBXNIYOKMPTIGPYZMDIKNHODLZBHMINVOGYGOGFULUNWMPFGGZTAXNKOENNTDWFURUGWZHMPNGQDZAYGOTIKLZICOGEBCBCOHUKOEWCYAGDVYKBCGNYGALIKDPGOHYNGIKLZICOGEBCBROTZUIPOCYDATYYKBCGNIKXWRCHURHIBYGOKMPTOAIXLKIYBBHBCIVCUHLFOZWZHQGAGDVYKBCGNIKVINHBIGYYKMPGOHYNGIKLZICOGEBCBZOROIGSUWLHUAGDVYKVURGHONVMGEWITIYYGIMGATYYKAYZRHUROIFALDIAGDVYKBCGNIKUITOOIVNHYNVVHOPYGOTKCZVWZWHYKHTDIWZITVZXNGOYKHTDIWZITVZXHHLXNYGALIKDPGOCHZNLZYIOKLCZHIQOECHNCXFKRTYYKYDNXCHAGDVYKEWBCGNYGGMIYGQNUCABGIGXPAGDVYKLAAYEFTIOFZIZVHKZHCPHYNGWCLZGPWZUFNHXN"

quadgram_frequencies, score_floor = quadgram_scorer.load_quadgram_frequencies("quadgrams.txt")

top_key = None
top_score = None

parent_key = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

def playfair_row(letter, key):
    # returns 0 to 4
    return int(key.index(letter) / 5)

def playfair_column(letter, key):
    # returns 0 to 4
    return int(key.index(letter) % 5)

def get_playfair_element(row, column, key):
    row = int(row) % 5
    column = int(column) % 5

    return key[row * 5 + column]

def playfair_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(int(len(ciphertext) / 2)):
        pair = ciphertext[i*2:i*2+2]

        a, b = pair[0], pair[1]
        a_column, a_row = playfair_column(a, key), playfair_row(a, key)
        b_column, b_row = playfair_column(b, key), playfair_row(b, key)

        if a_column == b_column:
            a = get_playfair_element(a_row - 1, a_column, key)
            b = get_playfair_element(b_row - 1, b_column, key)
        elif a_row == b_row:
            a = get_playfair_element(a_row, a_column - 1, key)
            b = get_playfair_element(b_row, b_column - 1, key)
        else:
            a = get_playfair_element(a_row, b_column, key)
            b = get_playfair_element(b_row, a_column, key)

        plaintext += "{}{}".format(a, b)

    return plaintext

def swap_two_random_elements(list_):
    swap_a, swap_b = random.sample(range(len(list_)), 2)
    list_[swap_a], list_[swap_b] = list_[swap_b], list_[swap_a]

def randomize_key(key):
    original_key = key[:]

    r = random.randint(0, 5)
    if r == 0:
        # reverse key
        key.reverse()
    elif r == 1:
        # reverse rows
        for row in range(5):
            for col in range(5):
                key[row * 5 + col] = original_key[(4 - row) * 5 + col]
    elif r == 2:
        # reverse columns
        for col in range(5):
            for row in range(5):
                key[row * 5 + col] = original_key[(4 - row) * 5 + col]
    elif r == 3:
        # swap 2 random rows
        row_a = random.randint(0, 4)
        row_b = random.randint(0, 4)
        for col in range(5):
            key[row_a * 5 + col] = key[row_b * 5 + col]
            key[row_b * 5 + col] = original_key[row_a * 5 + col]
    elif r == 4:
        # swap 2 random columns
        col_a = random.randint(0, 4)
        col_b = random.randint(0, 4)
        for row in range(5):
            key[row * 5 + col_a] = key[row * 5 + col_b];
            key[row * 5 + col_b] = original_key[row * 5 + col_a]
    else:
        # swap 2 random elements
        swap_two_random_elements(key)

while True:
    randomize_key(parent_key)

    parent_plaintext = playfair_decrypt(ciphertext, parent_key)
    parent_score = quadgram_scorer.quadgram_score(quadgram_frequencies, score_floor, parent_plaintext)

    iterations_without_improvement = 0
    while iterations_without_improvement < 1000:
        child_key = parent_key[:]
        randomize_key(child_key)

        child_plaintext = playfair_decrypt(ciphertext, child_key)
        child_score = quadgram_scorer.quadgram_score(quadgram_frequencies, score_floor, child_plaintext)

        if child_score > parent_score:
            parent_score = child_score
            parent_key = child_key
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

    if top_score is None or parent_score > top_score:
        top_score = parent_score
        top_key = parent_key[:]

        print("Top score:", top_score)
        print("Top key:", top_key)
        print("Top message:", playfair_decrypt(ciphertext, top_key))
