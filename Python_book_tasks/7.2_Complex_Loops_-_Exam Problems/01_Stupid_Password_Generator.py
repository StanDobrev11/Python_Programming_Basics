x = int(input())
y = int(input())

for a in range(1, x):
    for b in range(1, x):
        for c in range(ord("a"), ord("a") + y):  # letter
            for d in range(ord("a"), ord("a") + y):  # letter
                for e in range(1, x + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")

# 11aa2 11aa3 11aa4 11ab2 11ab3 11ab4
# 11ba2 11ba3 11ba4 11bb2 11bb3 11bb4
# 12aa3 12aa4 12ab3 12ab4 12ba3 12ba4
# 12bb3 12bb4 13aa4 13ab4 13ba4 13bb4
# 21aa3 21aa4 21ab3 21ab4 21ba3 21ba4
# 21bb3 21bb4 22aa3 22aa4 22ab3 22ab4
# 22ba3 22ba4 22bb3 22bb4 23aa4 23ab4
# 23ba4 23bb4 31aa4 31ab4 31ba4 31bb4
# 32aa4 32ab4 32ba4 32bb4 33aa4 33ab4
# 33ba4 33bb4
#
# 11aa2 11aa3 11aa4 11ab2 11ab3 11ab4
# 11ba2 11ba3 11ba4 11bb2 11bb3 11bb4
# 12aa3 12aa4 12ab3 12ab4 12ba3 12ba4
# 12bb3 12bb4 13aa4 13ab4 13ba4 13bb4
# 21aa3 21aa4 21ab3 21ab4 21ba3 21ba4
# 21bb3 21bb4 22aa3 22aa4 22ab3 22ab4
# 22ba3 22ba4 22bb3 22bb4 23aa4 23ab4
# 23ba4 23bb4 31aa4 31ab4 31ba4 31bb4
# 32aa4 32ab4 32ba4 32bb4 33aa4 33ab4
# 33ba4 33bb4
