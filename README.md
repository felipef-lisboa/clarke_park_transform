# Transformadas de Clarke e Park
[![N|Solid](http://www.cefet-rj.br/arquivos_download/logo_cefet__home_site.jpg)](http://www.cefet-rj.br/)

## Transformada de Clarke
> "Em engenharia elétrica, a transformada alpha-beta(α-β-γ), também conhecida como transformada de Clarke, é uma transformação matemática aplicada para simplificar a análise de circuitos trifásicos. Conceitualmente ela é similar a transformada dq0. Uma aplicação muito útil da transformada alpha-beta é a geração de um sinal de referência usado para [controle da modulação do vetor espacial](https://en.wikipedia.org/wiki/Space_vector_modulation)."
[traduzido da Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_transformation)

![eixos de clarke](https://www.mathworks.com/help/physmod/sps/ref/clarke_transform_axes_01.png) ![eixos2 de clarke](https://www.mathworks.com/help/physmod/sps/ref/clarke_transform_axes_02.png)
(Fonte: [Mathworks](https://www.mathworks.com/help/physmod/sps/ref/clarketransform.html))

A Transformada de Clarke consiste em um sistema cujo eixo alpha está completamente alinhado com a fase A e o eixo beta está em quadratura com este. Isso fornece duas curvas senoidais defasadas de 90 graus. Quando o sistema trifásico está em equilíbrio essas duas curvas em alpha-beta tem módulo igual. Quando o sistema desequilibra os módulos se tornam diferentes.

![](https://www.mathworks.com/help/physmod/sps/ref/clarke_transform_model_scope_01.png)
(Fonte: [Mathworks](https://www.mathworks.com/help/physmod/sps/ref/clarketransform.html))

## Trasformada de Park

> A ransformação direto-quadratura-zero (dq0) é um tensor que rotaciona o eixo de referência de um sistema vetorial de três elementos ou uma matriz de três por três elementos com o intuito de simplificar a análise. A transformada dq0 é o produto da transformada de Clarke e de Park, primeiramente proposto po Robert H. Park em 1929.
[traduzido da Wikipedia](https://en.wikipedia.org/wiki/Direct-quadrature-zero_transformation)

![eixos de park](https://www.mathworks.com/help/physmod/sps/ref/park_transform_axes_01.png) ![eixos2 de park](https://www.mathworks.com/help/physmod/sps/ref/park_transform_axes_02.png)
(fonte: [MathWorks](https://www.mathworks.com/help/physmod/sps/ref/parktransform.html))

A transformada de Park, quando aplicada a um sistema trifásico equilibrado, apresenta valores de d, q e zero constantes. Quando um desequilíbrio surge esses valores começam a oscilar (com o dobro da frequência do sistema original).
No momento de calcular a transformada de Park podemos alinhar com a fase A do nosso sistema trifásico o eixo d ou o eixo q. Neste projeto o eixo escolhido para alinhar com a fase A foi o eixo d, que resulta em um gráfico similar ao mostrado abaixo.

![grafico resultante](https://www.mathworks.com/help/physmod/sps/ref/park_transform_q_model_scope_01.png)
(fonte: [MathWorks](https://www.mathworks.com/help/physmod/sps/ref/parktransform.html))
