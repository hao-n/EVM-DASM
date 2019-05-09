opCodes = {
    '00': 'STOP',
    '01': 'ADD',
    '02': 'MUL',
    '03': 'SUB',
    '04': 'DIV',
    '05': 'SDIV',
    '06': 'MOD',
    '07': 'SMOD',
    '08': 'ADDMOD',
    '09': 'MULMOD',
    '0a': 'EXP',
    '0b': 'SIGNEXTEND',
    '10': 'LT',
    '11': 'GT',
    '12': 'SLT',
    '13': 'SGT',
    '14': 'EQ',
    '15': 'ISZERO',
    '16': 'AND',
    '17': 'OR',
    '18': 'XOR',
    '19': 'NOT',
    '1a': 'BYTE',
    '20': 'SHA3',
    '30': 'ADDRESS',
    '31': 'BALANCE',
    '32': 'ORIGIN',
    '33': 'CALLER',
    '34': 'CALLVALUE',
    '35': 'CALLDATALOAD',
    '36': 'CALLDATASIZE',
    '37': 'CALLDATACOPY',
    '38': 'CODESIZE',
    '39': 'CODECOPY',
    '3a': 'GASPRICE',
    '3b': 'EXTCODESIZE',
    '3c': 'EXTCODECOPY',
    '3d': 'RETURNDATASIZE',
    '3e': 'RETURNDATACOPY',
    '40': 'BLOCKHASH',
    '41': 'COINBASE',
    '42': 'TIMESTAMP',
    '43': 'NUMBER',
    '44': 'DIFFICULTY',
    '45': 'GASLIMIT',
    '50': 'POP',
    '51': 'MLOAD',
    '52': 'MSTORE',
    '53': 'MSTORE8',
    '54': 'SLOAD',
    '55': 'SSTORE',
    '56': 'JUMP',
    '57': 'JUMPI',
    '58': 'PC',
    '59': 'MSIZE',
    '5a': 'GAS',
    '5b': 'JUMPDEST',
    '60': 'PUSH1',
    '61': 'PUSH2',
    '62': 'PUSH3',
    '63': 'PUSH4',
    '64': 'PUSH5',
    '65': 'PUSH6',
    '66': 'PUSH7',
    '67': 'PUSH8',
    '68': 'PUSH9',
    '69': 'PUSH10',
    '6a': 'PUSH11',
    '6b': 'PUSH12',
    '6c': 'PUSH13',
    '6d': 'PUSH14',
    '6e': 'PUSH15',
    '6f': 'PUSH16',
    '70': 'PUSH17',
    '71': 'PUSH18',
    '72': 'PUSH19',
    '73': 'PUSH20',
    '74': 'PUSH21',
    '75': 'PUSH22',
    '76': 'PUSH23',
    '77': 'PUSH24',
    '78': 'PUSH25',
    '79': 'PUSH26',
    '7a': 'PUSH27',
    '7b': 'PUSH28',
    '7c': 'PUSH29',
    '7d': 'PUSH30',
    '7e': 'PUSH31',
    '7f': 'PUSH32',
    '80': 'DUP1',
    '81': 'DUP2',
    '82': 'DUP3',
    '83': 'DUP4',
    '84': 'DUP5',
    '85': 'DUP6',
    '86': 'DUP7',
    '87': 'DUP8',
    '88': 'DUP9',
    '89': 'DUP10',
    '8a': 'DUP11',
    '8b': 'DUP12',
    '8c': 'DUP13',
    '8d': 'DUP14',
    '8e': 'DUP15',
    '8f': 'DUP16',
    '90': 'SWAP1',
    '91': 'SWAP2',
    '92': 'SWAP3',
    '93': 'SWAP4',
    '94': 'SWAP5',
    '95': 'SWAP6',
    '96': 'SWAP7',
    '97': 'SWAP8',
    '98': 'SWAP9',
    '99': 'SWAP10',
    '9a': 'SWAP11',
    '9b': 'SWAP12',
    '9c': 'SWAP13',
    '9d': 'SWAP14',
    '9e': 'SWAP15',
    '9f': 'SWAP16',
    'a0': 'LOG0',
    'a1': 'LOG1',
    'a2': 'LOG2',
    'a3': 'LOG3',
    'a4': 'LOG4',
    'f0': 'CREATE',
    'f1': 'CALL',
    'f2': 'CALLCODE',
    'f3': 'RETURN',
    'f4': 'DELEGATECALL',
    'f5': 'CALLBLACKBOX',
    'fa': 'STATICCALL',
    'fd': 'REVERT',
    'fe': 'INVALID',
    # 'ff' : 'SUICIDE',
    'ff': 'SELFDESTRUCT',
}

push_map = {
    '60': 1,
    '61': 2,
    '62': 3,
    '63': 4,
    '64': 5,
    '65': 6,
    '66': 7,
    '67': 8,
    '68': 9,
    '69': 10,
    '6a': 11,
    '6b': 12,
    '6c': 13,
    '6d': 14,
    '6e': 15,
    '6f': 16,
    '70': 17,
    '71': 18,
    '72': 19,
    '73': 20,
    '74': 21,
    '75': 22,
    '76': 23,
    '77': 24,
    '78': 25,
    '79': 26,
    '7a': 27,
    '7b': 28,
    '7c': 29,
    '7d': 30,
    '7e': 31,
    '7f': 32,
}

def print_gap(choice):
    '''
    +--------+-------------------+
    | Choice | Output            |
    +--------+-------------------+
    | 0      | Deployment Opcode |
    +--------+-------------------+
    | 1      | Contract Opcode   |
    +--------+-------------------+
    | 2      | ?                 |
    +--------+-------------------+
    | 3      | bzzr code         |
    +--------+-------------------+
    | 4      | ABI Augs          |
    +--------+-------------------+
    '''
    if choice == 0:
        print('\n\n')
        print('***********************************', end='')
        print('***********************************')
        print('Deployment Opcode')
        print('***********************************', end='')
        print('***********************************')
    if choice == 1:
        print('\n\n')
        print('***********************************', end='')
        print('***********************************')
        print('Contract Opcode')
        print('***********************************', end='')
        print('***********************************')
    if choice == 2:
        print('\n\n')
        print('***********************************', end='')
        print('***********************************')
        print('What\'s this? ("00" is trivial)')
        print('***********************************', end='')
        print('***********************************')
    if choice == 3:
        print('\n\n')
        print('***********************************', end='')
        print('***********************************')
        print('bzzr code')
        print('***********************************', end='')
        print('***********************************')
    if choice == 4:
        print('\n\n')
        print('***********************************', end='')
        print('***********************************')
        print('ABI Augs')
        print('***********************************', end='')
        print('***********************************')