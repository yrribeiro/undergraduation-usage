# -- -- PRIMEIRA QUESTÃO
info = c(48, 58, 56, 63, 52, 50, 59, 51, 59, 38, 57, 56, 73, 61, 41, 
         55, 49, 61, 49, 49, 52, 55, 60, 52, 54, 57, 47, 66, 60, 53, 
         59, 50, 45, 57, 64, 56, 57, 60, 47, 58, 53, 58, 66, 47, 40.)
sort(info)

# -- Histograma com a frequência absoluta
freq_absoluta = table(info)
hist(
  info, 
  xlim=c(30, 80), 
  ylim=c(0, 20),
  ylab='Frequência', 
  xlab='Idade', 
  main='Frequência de idade'
)

# -- Média, mediana, percentis e moda
summary(info)

percen8 = quantile(info, probs=0.08)
percen50 = quantile(info, probs=0.5)
percen80 = quantile(info, probs=0.8)
percen25 = quantile(info, probs=0.25)
percen75 = quantile(info, probs=0.75)

all_percen = c(percen8, percen50, percen80)
all_percen

# -- Moda de Czuber
czuber = function(y){
  uni_y = unique(y)
  uni_y[which.max(tabulate(match(y, uni_y)))]
}

moda_c = czuber(info)
moda_c
# -- Boxplot
boxplot(info, xlab='Idades', col='orange', border='brown', horizontal=TRUE)

# -- -- SEGUNDA QUESTÃO
df = read.csv(file = "~/Desktop/Ufal/Estatística/dadosPacientes2021.csv")
str(df)

# -- Situação Atual
data = table(df["situacao_atual"])
names(data)[3] = c("Encerramento 
                   do Isolamento 
                   Domiciliar")

names(data)[4] = c("Internação
                   Leito Clínic")

names(data)[6] = c("Isolamento
                   Domiciliar")

names(data)[8] = c("óbito por
                   outras causas")
data
par(las=2)
barplot(data, cex.names = 0.7)

# -- Óbitos por município
obitos = df[df$situacao_atual == "Óbito",]

municipio = sort(municipio)

names(municipio)[100] = c("Marechal
                          Deodoro")

names(municipio)[101] = c("Palmeiras
                          dos Índios")
par(las=2)
barplot(municipio[100:104], cex.names = 0.8)

# -- Relação - Idade, óbito e gênero
obitos = df[df$situacao_atual == "Óbito",]
obitos$sexo[obitos$sexo == "Mascuino"] = "Masculino"
obitos = obitos[obitos$idade>=0,]
sexo = table(obitos[3])
idade = table(obitos[10])
sexo
idade
x <- xtabs(~sexo + idade, data = obitos)
x
par(las=1)

barplot(x,
        beside = FALSE,
        xlab = "Idade",
        legend.text = rownames(x),
        ylab = "Óbitos",
        col = c("blue", "red"))
box(bty = "L")

# -- Histograma - Óbitos por idade
obitos = df[df$situacao_atual == "Óbito",]

idade = table(obitos[10])
hist(
  idade,
  main='Histograma de óbitos por idade',
  col = 'pink',
  labels = TRUE,
  ylim = c(0,50),
  xlim = c(0, 110),
  ylab = 'Frequência',
  xlab = 'Idade'
)

# -- Barras, óbitos por mês
data <- data.frame(
  "Data Obito"=obitos$data_resultado_exame, 
  obitos$situacao_atual=="Óbito"
)
data.tb<- as.Date(data$Data.Obito)
data.mes <- table(months(data.tb))
par(las=3)
ordered_months = c(
  "janeiro",
  "fevereiro",
  "março", 
  "abril",
  "maio", 
  "junho", 
  "julho", 
  "agosto", 
  "setembro", 
  "outubro", 
  "novembro", 
  "dezembro"
)
barplot(data.mes[ordered_months])

# ---- TERCEIRA QUESTÃO
# -- Internação X etnia
pdi = df[df$municipio_residencia == "Palmeira dos Índios",]
uti = pdi[pdi$situacao_atual == "Internação UTI"]
new_uti = subset(uti, select=-c(1, 3, 4, 5, 6, 7, 8, 9))
pie(
  table(new_uti$etnia),
  main='Internação em UTI por etnia',
  col=c('yellow', 'pink', 'gray', 'red', 'brown')
)

# -- Internação >= 40
interclin = pdi[pdi$situacao_atual == "Internação Leito Clínico" 
                | pdi$situacao_atual == "Internação UTI" 
                & pdi$idade >= 40,]
new_df = subset(interclin, select = -c(1, 2, 4, 5, 6, 7, 8, 9))
x = xtabs(~sexo + idade, data = new_df)
barplot(
  table(new_df),
  main='Internações (clínico e UTI) a partir de 40 anos',
  col=c('yellow', 'blue'),
  legend.text = rownames(x),
)

# -- Óbitos abaixo de 45 anos
obitos = pdi[pdi$situacao_atual == "Óbito" & pdi$idade < 45,]

obitosacima = pdi[pdi$situacao_atual == "Óbito" & pdi$idade >= 45,]

obito_total = pdi[pdi$situacao_atual == "Óbito",]

prop = (nrow(obitos)/nrow(obito_total))*100
prop_acima = (nrow(obitosacima)/nrow(obito_total))*100

pie(
  c(prop, prop_acima),
  main='Proporção de óbitos abaixo de 45 anos',
  labels = '11%',
  col=c('red', 'gray'),
  
)
