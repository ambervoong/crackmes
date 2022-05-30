#!/usr/bin/env python
# coding: utf-8
# Link to crackme: https://crackmes.one/crackme/6165bf9e33c5d4329c345108
# In[104]:


def calculateUsernameByte(password, n, i):
    usernamelength = 8 # hardcoded for problem
    alphabet_string = 'ABCDEFGH'
    return int((0x1a * n) + (ord(password[i]) - 0x41) + ord(password[i-1]) - usernamelength - ord(alphabet_string[i]) - i)
def retrieveUsername(n, password='AFMWAFPE'):
    # first character
    username_firstbyte = 0x7a - (n * 0x1a)
    if username_firstbyte > 64 and username_firstbyte < 90:
        username = [chr(username_firstbyte)]
    else: 
        return None
    # rest of the characters
    for i in range(1, 8):
        username_byte = calculateUsernameByte(password, n, i)
        # Note that the username can only be uppercase, so 65-90 in ASCII
        while username_byte < 65:
            n += 1
            username_byte = calculateUsernameByte(password, n, i)
        while username_byte > 90:
            n -= 1
            username_byte = calculateUsernameByte(password, n, i)
        if username_byte > 64 and username_byte < 90:
            username.append(chr((username_byte)))
    return ''.join(username)


# In[163]:


def originalPwdGenerator(username):
    usernamelength = 8 # hardcoded for problem
    alphabet_string = 'ABCDEFGH'
    # We skipped the ASCII bounds checking, this assumes the username is correct
    password = [chr(int(((0x7a - ord(username[0])) % 0x1a + 0x41)))]
    for i in range(1, 8):
        password.append(chr(int(((ord(alphabet_string[i]) + (i) + ord(username[i])) - ord(password[i-1]) + usernamelength) % 0x1a + 0x41)))
    return ''.join(password)


# ###### 

# In[170]:


if __name__ == '__main__':
    allusrs = [retrieveUsername(n, 'AFMWAFPE') for n in range(10)]
    username = [x for x in allusrs if x is not None]
    print('The given password AFMWAFPE was generated from username %s.' % (username[0]))
    print('Using username %s, the original password generator would have outputted password %s.' % (username, originalPwdGenerator(username[0])))   

