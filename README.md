# MTOption  

Utilitário de linha de comando para operações com opções utilizando o MetaTrader5.  

------------

## Pré-requisitos  

* [MetaTrader5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [API.ex5](https://drive.google.com/file/d/1Osofc0PfxHpKk6FVCVucaSGnlmSPtnaL/view?usp=sharing) - Expert advisor executando no MetaTrader5.  
* [Python](https://www.python.org/downloads/windows) - Interpretador de comandos disponível no prompt de comando.  

## Instalação

```
> pip install mtoption
```

## Comandos  

### op bullspread  
Exibe dados de uma trava de alta.  
```
op bullspread <opcao1> <opcao2>  
ou  
ta <opcao1> <opcao2>  
```
Exibe dados da trava de alta com opcao1 e opcao2.  
Exemplo:  
```
ta bovac110 bovac109  
```
resultado:  
Bull Spread  
venda BOVAC110 0.14  
compra BOVAC109 0.17  
saldo -0.03  
