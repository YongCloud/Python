'''
Unravel the mysterious message from the Buggarians.
The last message received from the extraterrestrials visitors is as follows.
220 241 255 245 052 313
311 052 312 303 052 312
252 245 052 205 241 251
253 243 052 203 253 302
251 244 303 301 053
'''
# source message, remove prefix 0
src = 220,241,255,245,52,313,311,52,312,\
    303,52,312,252,245,52,205,241,251,253,243,\
    52,203,253,302,251,244,303,301,53
# decipher the message
for x in src:
    # decode to decimal number with base 6
    dec = x // 100 * 36 + x % 100 // 10 * 6 + x % 10
    # decode to ASCII text
    print(chr(dec),end='')
# result: Take us to the Magic Kingdom!
