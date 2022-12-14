#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: _SM4.py
# @time: 2018/9/21 15:25
# @Software: PyCharm


"""
SM4 GM
@author: Dawei
@author: A.Star
"""
import copy
import struct
import time
from functools import reduce

# Expanded SM4 S-boxes    Sbox table: 8bits input convert to 8 bits output
SboxTable = [
    0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05,
    0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
    0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62,
    0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6,
    0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8,
    0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35,
    0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87,
    0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e,
    0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1,
    0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3,
    0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f,
    0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51,
    0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8,
    0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0,
    0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84,
    0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48,
]

# System parameter
FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc]

# fixed parameter
CK = [
    0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
    0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
    0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
    0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
    0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
    0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
    0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
    0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279
]

ENCRYPT = 0
DECRYPT = 1


def GET_UINT32_BE(key_data):
    return int((key_data[0] << 24) | (key_data[1] << 16) | (key_data[2] << 8) | (key_data[3]))


def PUT_UINT32_BE(n):
    return [int((n >> 24) & 0xff), int((n >> 16) & 0xff), int((n >> 8) & 0xff), int((n) & 0xff)]


# rotate shift left marco definition
def SHL(x, n):
    return int(int(x << n) & 0xffffffff)


def ROTL(x, n):
    return SHL(x, n) | int((x >> (32 - n)) & 0xffffffff)


def XOR(a, b):
    return list(map(lambda x, y: x ^ y, a, b))


# look up in SboxTable and get the related value.
# args:    [in] inch: 0x00~0xFF (8 bits unsigned value).
def sm4Sbox(idx):
    return SboxTable[idx]


# Calculating round encryption key.
# args:    [in] a: a is a 32 bits unsigned value;
# return: sk[i]: i{0,1,2,3,...31}.
def sm4CalciRK(ka):
    a = PUT_UINT32_BE(ka)
    b = [sm4Sbox(i) for i in a]
    bb = GET_UINT32_BE(b)
    rk = bb ^ (ROTL(bb, 13)) ^ (ROTL(bb, 23))
    return rk


# private F(Lt) function:
# "T algorithm" == "L algorithm" + "t algorithm".
# args:    [in] a: a is a 32 bits unsigned value;
# return: c: c is calculated with line algorithm "L" and nonline algorithm "t"
def sm4Lt(ka):
    a = PUT_UINT32_BE(ka)
    b = [sm4Sbox(i) for i in a]
    bb = GET_UINT32_BE(b)
    return bb ^ (ROTL(bb, 2)) ^ (ROTL(bb, 10)) ^ (ROTL(bb, 18)) ^ (ROTL(bb, 24))


# private F function:
# Calculating and getting encryption/decryption contents.
# args:    [in] x0: original contents;
# args:    [in] x1: original contents;
# args:    [in] x2: original contents;
# args:    [in] x3: original contents;
# args:    [in] rk: encryption/decryption key;
# return the contents of encryption/decryption contents.
def sm4F(x0, x1, x2, x3, rk):
    return x0 ^ sm4Lt(x1 ^ x2 ^ x3 ^ rk)


class Sm4(object):
    def __init__(self):
        self.sk = [0] * 32
        self.mode = ENCRYPT

    def sm4_set_key(self, key_data, mode):
        self.sm4_setkey(key_data, mode)

    def sm4_setkey(self, key, mode):
        k = [0] * 36
        MK = struct.unpack_from(">IIII", bytes(key))
        k[0:4] = XOR(MK, FK)
        item = k[1] ^ k[2]
        for i in range(32):
            item ^= k[i + 3]
            k[i + 4] = k[i] ^ sm4CalciRK(item ^ CK[i])
            item ^= k[i + 1]
        self.sk = k[4:]
        self.mode = mode
        if mode == DECRYPT:
            self.sk.reverse()

    def sm4_one_round(self, sk, in_put):
        item = list(struct.unpack_from(">IIII", bytes(in_put)))
        item.reverse()
        res = reduce(lambda x, y: [sm4F(x[3], x[2], x[1], x[0], y), x[0], x[1], x[2]], sk, item)
        rev2 = reduce(lambda x, i: x+struct.pack(">I", i), res, b'')
        return list(rev2)

    def sm4_crypt_ecb(self, input_data):
        # SM4-ECB block encryption/decryption
        tmp = [input_data[i:i + 16] for i in range(0, len(input_data), 16)]
        output_data = reduce(lambda a, b: a + b, map(lambda x: self.sm4_one_round(self.sk, x), tmp), [])
        return output_data

    def sm4_crypt_cbc(self, iv, input_data):
        # SM4-CBC buffer encryption/decryption
        length = len(input_data)
        i = 0
        output_data = []
        tmp_input = [0] * 16
        if self.mode == ENCRYPT:
            while length > 0:
                tmp_input[0:16] = XOR(input_data[i:i + 16], iv[0:16])
                output_data += self.sm4_one_round(self.sk, tmp_input[0:16])
                iv = copy.deepcopy(output_data[i:i + 16])
                i += 16
                length -= 16
        else:
            ivs = [input_data[i:i + 16] for i in range(0, len(input_data), 16)]
            ivs.insert(0, iv)
            tmp = map(lambda x: self.sm4_one_round(self.sk, x), ivs[1:])
            output_data = reduce(lambda a, b: a + b, map(XOR, tmp, ivs[:-1]), [])
        return output_data

    def sm4_crypt_pcbc(self, iv, input_data):
        """
        SM4-PCBC buffer encryption/decryption
        :param iv:
        :param input_data:
        :return:
        """
        length = len(input_data)
        i = 0
        output_data = []
        if self.mode == ENCRYPT:
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, XOR(iv, tmp_input[0:16]))
                output_data.extend(out)
                iv = copy.deepcopy(XOR(out, tmp_input))
                i += 16
                length -= 16
        else:
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, tmp_input[0:16])
                out = XOR(out, iv)
                iv = copy.deepcopy(XOR(out, tmp_input))
                output_data.extend(out)
                i += 16
                length -= 16
        return output_data

    def sm4_crypt_ofb(self, iv, input_data):
        """
        SM4-OFB buffer encryption/decryption
        :param iv:
        :param input_data:
        :return:
        """
        length = len(input_data)
        i = 0
        output_data = []
        if self.mode == ENCRYPT:
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, iv)
                iv = out
                out = XOR(out, tmp_input)
                output_data.extend(out)
                i += 16
                length -= 16
        else:
            self.mode = ENCRYPT
            self.sk = self.sk[::-1]
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, iv)
                iv = out
                out = XOR(out, tmp_input)
                output_data.extend(out)
                i += 16
                length -= 16
            self.mode = DECRYPT
            self.sk = self.sk[::-1]
        return output_data

    def sm4_crypt_cfb(self, iv, input_data):
        """
        SM4-CFB buffer encryption/decryption
        :param iv:
        :param input_data:
        :return:
        """
        length = len(input_data)
        i = 0
        output_data = []
        if self.mode == ENCRYPT:
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, iv)
                iv = XOR(tmp_input, out)
                output_data.extend(iv)
                i += 16
                length -= 16
        else:
            self.mode = ENCRYPT
            self.sk = self.sk[::-1]
            while length > 0:
                tmp_input = input_data[i:i + 16]
                out = self.sm4_one_round(self.sk, iv)
                out = XOR(out, tmp_input)
                iv = tmp_input
                output_data.extend(out)
                i += 16
                length -= 16
            self.mode = DECRYPT
            self.sk = self.sk[::-1]
        return output_data


def sm4_crypt_ecb(mode, key, data):
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key, mode)
    en_data = sm4_d.sm4_crypt_ecb(data)
    return en_data


def sm4_crypt_cbc(mode, key, iv, data):
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key, mode)
    en_data = sm4_d.sm4_crypt_cbc(iv, data)
    return en_data


def sm4_crypt_pcbc(mode, key, iv, data):
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key, mode)
    en_data = sm4_d.sm4_crypt_pcbc(iv, data)
    return en_data


def sm4_crypt_cfb(mode, key, iv, data):
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key, mode)
    en_data = sm4_d.sm4_crypt_cfb(iv, data)
    return en_data


def sm4_crypt_ofb(mode, key, iv, data):
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key, mode)
    en_data = sm4_d.sm4_crypt_ofb(iv, data)
    return en_data



SM4 = Sm4

if __name__ == "__main__":
    # log_init()
    import numpy as np
    input_data = list(np.random.randint(256, size=1024*6))
    iv_data = [0] * 16
    time.clock()
    sm4_d = Sm4()
    key_data = b'hello world, errr...'
    # key_data = [0x5a] * 16
    sm4_d.sm4_set_key(key_data, ENCRYPT)
    st = time.clock()
    en_data = sm4_d.sm4_crypt_ecb(input_data)
    print(en_data, "en_data:")
    sm4_d.sm4_set_key(key_data, DECRYPT)
    de_data = sm4_d.sm4_crypt_ecb(en_data)
    print(de_data, "de_data:")
    if de_data == input_data:
        print("ecb check pass")
    else:
        print("ecb check fail")
        raise BaseException("error")
    et = time.clock()
    print(et-st)
    sm4_d.sm4_set_key(key_data, ENCRYPT)
    en_data = sm4_d.sm4_crypt_cbc(iv_data, input_data)
    print(en_data, "en_data:")
    sm4_d.sm4_set_key(key_data, DECRYPT)
    de_data = sm4_d.sm4_crypt_cbc(iv_data, en_data)
    print(de_data, "de_data:")
    if de_data == input_data:
        print("cbc check pass")
    else:
        print("cbc check fail")
        raise BaseException("error")
    # file test
    file_path = r"../../test2.txt"
    ecb_path_en = r"../../test2k_ecb_en.txt"
    ecb_path_de = r"../../test2k_ecb_de.txt"
    cbc_path_en = r"../../test2k_cbc_en.txt"
    cbc_path_de = r"../../test2k_cbc_de.txt"

    key_data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
    iv_data = [0x5a] * 16

    with open(file_path, 'rb') as f:
        file_data = f.read()
    # file_data_list = [ord(x) for x in file_data]
    file_data_list = list(file_data)
    # 1. ECB
    sm4_d = Sm4()
    sm4_d.sm4_set_key(key_data, ENCRYPT)
    en_data = sm4_d.sm4_crypt_ecb(file_data_list)
    with open(ecb_path_en, 'wb') as f:
        f.write(bytes(en_data))

    sm4_d.sm4_set_key(key_data, DECRYPT)
    de_data = sm4_d.sm4_crypt_ecb(en_data)
    with open(ecb_path_de, 'wb') as f:
        f.write(bytes(de_data))
    if de_data == file_data_list:
        print("file decode pass")
    else:
        print("file decode fail")
        raise BaseException('error')

    # 2. CBC
    sm4_d.sm4_set_key(key_data, ENCRYPT)
    en_data = sm4_d.sm4_crypt_cbc(iv_data, file_data_list)
    with open(cbc_path_en, 'wb') as f:
        f.write(bytes(en_data))

    sm4_d.sm4_set_key(key_data, DECRYPT)
    de_data = sm4_d.sm4_crypt_cbc(iv_data, en_data)
    with open(cbc_path_de, 'wb') as f:
        f.write(bytes(de_data))
    if de_data == file_data_list:
        print("file decode pass")
    else:
        print("file decode fail")
        raise BaseException("error")
