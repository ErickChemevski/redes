Descrição:

Desenvolva um webcrawler HTTP/1.1 multithreaded, com um subconjunto da RFC 2616 [1]. O webcrawler recebe como parâmetro na linha de comando a profundidade de busca e uma URL. A partir disso, o webcrawler recursivamente busca a página e as páginas ligadas com tags < ahref > até o nível máximo especi?cado na profundidade de busca. As seguintes linguagens de programação podem ser usadas:
  C, C++ e Objective C
  Java
  Ruby
  Python
  Perl
  Shell script
Outras linguagens podem ser usadas desde que o professor seja consultado antes e esteja de acordo. Porém, bibliotecas,
componentes ou códigos disponíveis na Internet que implementem o protocolo HTTP não podem ser usados. Caso seja detectado
desrespeito a este detalhe, o trabalho receberá nota zero.Um script chamado executeme deve ser fornecido para disparar o programa. No máximo 8 threads devem executar em paralelo em um determinado instante. Não é necessário respeitar o arquivo robots.txt no servidor (embora seja desejável). Não é obrigatório o uso de threads, mas um adicional de 10% na nota será dado para os casos em que forem usadas (e o trabalho funcionar). O trabalho deve ser todo desenvolvido com o sistema de gerenciamento de versões git. Todas as modi?cações nos códigos devem ser registradas com comentários que façam sentido. Uma opção para compartilhar um repositório apenas com os colegas que fazem parte do grupo é usar o Sparkleshare. O trabalho pode ser feito em grupos de até 4 alunos, desde que seja possível identi?car commits de todos os integrantes do grupo com contribuição ao projeto.


Produtos

A entrega será realizadas pelo Ava, e devera conter:
  Fontes do programa e cópia do repositório do sistema de gerenciamento de versões;
  Make?le que gere o programa;
  Script para disparar o executável;
  README.txt contendo nome completo dos alunos e curso, descrevendo a implementação e os testes realizados.


