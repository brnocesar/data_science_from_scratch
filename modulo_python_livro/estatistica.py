# media aritmetica: soma dos dados dividida pela contagem
def mean(xs: list) -> float:
    return sum(xs) / len(xs)


# mediana -> mais dificil de calcular, preciso ordenar os dados (ou nao, ver quickselect)
def median(xs: list) -> float:
    n = len(xs)
    sorted_xs = sorted(xs)
    midpoint = n // 2 # divisao inteira

    if n % 2 == 1:
        return sorted_xs[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_xs[lo] + sorted_xs[hi]) / 2


# quantil: valor abaixo do qual esta uma certa porcentagem dos dados
def quantile(xs: list, p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


# moda: valores mais comuns
def mode(xs: list) -> list:
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


# medida da dispersao: AMPLITUDE dos dados
def data_range(xs: list) -> float:
    return max(xs) - min(xs)


# medida da dispersao: VARIANCIA -> medida de como uma variavel desvia de sua media

# produto escalar de dois vetores
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# soma dos quadrados de um vetor
def sum_of_squares(v):
    return dot(v, v)

def de_mean(xs: list) -> list:
    # centraliza os dados subtraindo a media de cada elemento, assim a nova lista tera media igual a zero
    x_medio = mean(xs)
    return [x - x_medio for x in xs]

def variance(xs: list) -> float:
    n = len(xs)
    assert n >= 2, "variance requires at least two elements"
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: list) -> float:
    return (variance(xs))**0.5

def coefficient_of_variation(xs: list) -> float:
    return standard_deviation(xs) / mean(xs)


# medida da dispersao: DIFERENCA ENTRE PERCENTIS
def interquartile_range(xs: list) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)


# mede como 2 variaveis variam em conjunto de suas medias
def covariance(xs: list, ys: list) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: list, ys: list) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0

