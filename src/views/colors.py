# Area destinada a importações

def cores():
    PRETO          = '\033[30m'
    VERMELHO       = '\033[31m'
    VERDE          = '\033[32m'
    AMARELO        = '\033[33m'
    AZUL           = '\033[34m'
    MAGENTA        = '\033[35m'
    CIANO          = '\033[36m'
    BRANCO         = '\033[37m'

    PRETO_CLARO    = '\033[90m'
    VERMELHO_CLARO = '\033[91m'
    VERDE_CLARO    = '\033[92m'
    AMARELO_CLARO  = '\033[93m'
    AZUL_CLARO     = '\033[94m'
    MAGENTA_CLARO  = '\033[95m'
    CIANO_CLARO    = '\033[96m'
    BRANCO_CLARO   = '\033[97m'

    RESET          = '\033[0m'

    return (PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO,
            PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO,
            MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET)