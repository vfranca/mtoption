# MTOption  

Utilitário de linha de comando para operações com opções utilizando o MetaTrader5.  

## Comandos  

### op bullspread  
Exibe dados de uma trava de alta de duas calls.  
```
op bullspread <call1> <call2>  
ou  
ta <call1> <call2>  
```
Exibe dados da trava de alta com call1 e call2.  
Exemplo:  
```
ta bovac110 bovac109  
```
resultado:  
bull spread  
venda BOVAC110 0.14  
compra BOVAC109 0.17  
premio 0.03  
