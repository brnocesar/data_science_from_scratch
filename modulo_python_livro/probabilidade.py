# ds_do_zero/probabilidade.py
__all__ = ["normal_pdf", "normal_cdf", "inverse_normal_cdf"]

import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    # mu: media
    # sigma: desvio-padrao
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """
    Encontra o inverso aproximado da CDF normal usando pesquisa binaria.
    """
    # se nao for normal padrao, computa o padrao e redimensiona
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    # 1) parte de um intervalo grande, que sabemos que a resposta certa esta dentro
    low_z = -10.0                       # normal_cdf(-10) (eh muito proxima de) 0
    hi_z  =  10.0                       # normal_cdf(+10) (eh muito proxima de) 1

    while hi_z - low_z > tolerance:

        # 2) testa  ponto medio
        mid_z = (low_z + hi_z) / 2      # considere o ponto medio
        mid_p = normal_cdf(mid_z)       # e o valor da CDF

        # 3) compara o resultado com a probabilidade dada
        if mid_p < p:
            # valor da CDF eh MENOR que a probabilidade desejada
            # o ponto medio eh muito baixo, procure um maior
            low_z = mid_z
        elif mid_p > p:
            # valor da CDF eh MAIOR que a probabilidade desejada
            # o ponto medio eh muito alto, procure um menor
            hi_z = mid_z
        else:
            break

    return mid_z

