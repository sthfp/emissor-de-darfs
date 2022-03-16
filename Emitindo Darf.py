#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from selenium import webdriver 
import pyautogui
from time import sleep

driver = webdriver.Chrome()
driver.get("https://sicalc.receita.economia.gov.br/sicalc/rapido/contribuinte")
driver.find_element_by_xpath('//*[@id="optionPJ"]').click()
driver.find_element_by_xpath('//*[@id="cnpjFormatado"]').send_keys({CNPJ_BU1})
sleep(1)
#clicar em Maximizar Tela
pyautogui.click(875,24)
sleep(1)
#clicar no Captcha
pyautogui.click(543,632)
sleep(3)
#clicar em Continuar
driver.find_element_by_xpath('//*[@id="divBotoes"]/input[1]').click()
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("1708 - 06 - ME - a partir de 01/01/2008 - IRRF - Remuneração Serviços Prestados por Pessoa Jurídica - IRRF - REMUNERAÇÃO DE SERVIÇOS PROFISSIONAIS PRESTADOS POR PJ")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(677,561);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(764,790)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(698,712)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
sleep(2)
#selecionando o item
pyautogui.click(497,763)
#emitindo darf
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
pyautogui.press('end')
#clicando em Excluir
pyautogui.click(847,772)
pyautogui.press('enter')
#centralizando a tela para cima
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(704,728, clicks=3)
pyautogui.press('delete')
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5952 - 07 - ME - a partir de 01/06/2015 - Retenção de Contribuições sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado - CSLL, Cofins e PIS - CSLL/COFINS/PIS/PASEP - RETENÇÃO DE CONTRIBUIÇÕES SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(689,505);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(770,708)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(690,657)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(496,708)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(847,774)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(704,728, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5960 - 07 - ME - a partir de 01/06/2015 - Cofins - Retenção sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado (art. 30 da Lei nº 10.833/2003) - COFINS - RETENÇÃO SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(774,731)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("0588 - 06 - ME - a partir de 01/01/2008 - IRRF - Rendimento do Trabalho sem Vínculo Empregatício - IRRF - REND DO TABALHO SEM VÍNCULO EMPREGATÍCIO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(768,760)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("3280 - 06 - ME - a partir de 01/01/2008 - IRRF - Rem Serv Prest Associad Coop Trabalho - IRRF - SERV PREST POR ASSOC DE COOP DE TRABALHO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(766,813)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("8045 - 06 - ME - a partir de 01/01/2008 - IRRF - Outros Rendimentos - IRRF - COMISSÕES E CORRETAGENS PAGOS À PJ/SERVIÇOS DE PROPAGANDA PRESTADOS POR PJ")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(775,840)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)



#### BU2 ####

#Atualizando a Página
driver.refresh();
#Fechando a página de Downloads Abertos
##Step Importante, pois caso ela permaneça aberta, vai alterar todos os posicionamentos dos mouses
pyautogui.click(1903,1011)

driver.find_element_by_xpath('//*[@id="optionPJ"]').click()
driver.find_element_by_xpath('//*[@id="cnpjFormatado"]').send_keys({CNPJ_BU2})
sleep(2)
#clicar no Captcha
pyautogui.click(539,696)
sleep(3)
#clicar em Continuar
driver.find_element_by_xpath('//*[@id="divBotoes"]/input[1]').click()
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("1708 - 06 - ME - a partir de 01/01/2008 - IRRF - Remuneração Serviços Prestados por Pessoa Jurídica - IRRF - REMUNERAÇÃO DE SERVIÇOS PROFISSIONAIS PRESTADOS POR PJ")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(677,561);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(975,816)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(698,712)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
sleep(2)
#selecionando o item
pyautogui.click(497,763)
#emitindo darf
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
pyautogui.press('end')
#clicando em Excluir
pyautogui.click(847,772)
pyautogui.press('enter')
#centralizando a tela para cima
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(704,728, clicks=3)
pyautogui.press('delete')
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5952 - 07 - ME - a partir de 01/06/2015 - Retenção de Contribuições sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado - CSLL, Cofins e PIS - CSLL/COFINS/PIS/PASEP - RETENÇÃO DE CONTRIBUIÇÕES SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(689,505);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(971,709)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(690,657)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(496,708)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(847,774)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(704,728, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5960 - 07 - ME - a partir de 01/06/2015 - Cofins - Retenção sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado (art. 30 da Lei nº 10.833/2003) - COFINS - RETENÇÃO SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(980,759)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("0588 - 06 - ME - a partir de 01/01/2008 - IRRF - Rendimento do Trabalho sem Vínculo Empregatício - IRRF - REND DO TABALHO SEM VÍNCULO EMPREGATÍCIO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(971,784)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("3280 - 06 - ME - a partir de 01/01/2008 - IRRF - Rem Serv Prest Associad Coop Trabalho - IRRF - SERV PREST POR ASSOC DE COOP DE TRABALHO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(981,836)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(703,731, clicks=3)
pyautogui.press('delete')
sleep(1)
#############
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5979 - 07 - ME - a partir de 01/06/2015 - PIS - Retenção sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado - PIS/PASEP - RETENÇÃO SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(676,502);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(975,736)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(695,660)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(495,707)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
#clicando em Excluir
pyautogui.press('end')
pyautogui.click(848,773)
#centralizando a tela para cima
pyautogui.press('enter')
pyautogui.press('home')
sleep(1)


#### BU3 ####

#Atualizando a Página
driver.refresh();
#Fechando a página de Downloads Abertos
##Step Importante, pois caso ela permaneça aberta, vai alterar todos os posicionamentos dos mouses
pyautogui.click(1903,1011)

driver.find_element_by_xpath('//*[@id="optionPJ"]').click()
driver.find_element_by_xpath('//*[@id="cnpjFormatado"]').send_keys({CNPJ_BU3})
sleep(2)
#clicar no Captcha
pyautogui.click(539,696)
sleep(3)
#clicar em Continuar
driver.find_element_by_xpath('//*[@id="divBotoes"]/input[1]').click()
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("1708 - 06 - ME - a partir de 01/01/2008 - IRRF - Remuneração Serviços Prestados por Pessoa Jurídica - IRRF - REMUNERAÇÃO DE SERVIÇOS PROFISSIONAIS PRESTADOS POR PJ")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(677,561);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
#indo até o fim da tela para poder centralizar o clique
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(1208,710)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(698,712)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
sleep(2)
#selecionando o item
pyautogui.click(497,763)
#emitindo darf
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando a tela com end
pyautogui.press('end')
pyautogui.click(497,763)
sleep(10)
pyautogui.press('end')
#clicando em Excluir
pyautogui.click(847,772)
pyautogui.press('enter')
#centralizando a tela para cima
pyautogui.press('home')
sleep(1)
#apagando o campo de código para poder digitar outro
pyautogui.click(704,728, clicks=3)
pyautogui.press('delete')
sleep(1)
#digitar o Código do Imposto
driver.find_element_by_xpath('//*[@id="codReceitaPrincipal"]').send_keys("5952 - 07 - ME - a partir de 01/06/2015 - Retenção de Contribuições sobre Pagamentos de Pessoa Jurídica a Pessoa Jurídica de Direito Privado - CSLL, Cofins e PIS - CSLL/COFINS/PIS/PASEP - RETENÇÃO DE CONTRIBUIÇÕES SOBRE PAGAMENTOS DE PJ A PJ DE DIREITO PRIVADO")
sleep(1)
#selecionar o Código do Imposto
pyautogui.click(732,746)
sleep(2)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(732,746)
pyautogui.press('end')
sleep(1)
#preenchendo o mês/ano da apuração
pyautogui.click(689,505);pyautogui.typewrite('022022')
sleep(1)
#indo até a Base para copiar o valor apurado
pyautogui.hotkey('alt','tab')
sleep(1)
#pressionando para selecionar fora do campo (para possibiliar o "end")
pyautogui.click(1731,561)
pyautogui.press('end')
sleep(1)
#selecionando o valor apurado para este código na Base e copiando-o
pyautogui.doubleClick(1204,735)
pyautogui.hotkey('ctrl','c')
#mudando de tela para preencher no sicalcWeb o valor apurado para este código
pyautogui.hotkey('alt','tab')
pyautogui.press('end')
#indo até o campo de valor para dar dois cliques e colar
##Atenção: Esse campo é extremamente sensível, não sendo possível preencher a casa decimal através do typewrite
pyautogui.doubleClick(690,657)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
sleep(1)
#clicando em calcular
driver.find_element_by_xpath('//*[@id="btnCalcular"]').click()
sleep(1)
#centralizando a tela
pyautogui.press('end')
sleep(2)
#clicando em selecionar para emitir o DARF
pyautogui.click(496,708)
#emitir DARF
driver.find_element_by_xpath('//*[@id="btnDarf"]').click()
sleep(1)
#centralizando tela com end
pyautogui.press('end')
pyautogui.click(497,763)



#Validar Posição do Mouse

sleep(5)
pyautogui.position()


#Rodar a Planilha de Apuração aqui

apuracao=pd.read_excel(r"Impostos Federais.xlsx")
apuracao.drop(columns = ["Vazio"], inplace = True)
apuracao.drop(columns = ["Empty"], inplace = True)
apuracao.drop(columns = ["Unnamed: 0"], inplace = True)
display(apuracao)




