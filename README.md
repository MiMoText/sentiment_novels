# sentiment_novels

Sentiment analysis on french novels from the roman18 corpus in the context of the "Mining and Modeling Text" project (University Trier). www.mimotext.uni-trier.de


## Description

The roman18-corpus of about 100-200 eighteenth-century French novels in full text is analysed via two different Sentiment Analysis pipelines: [textblob fr](https://pypi.org/project/textblob-fr/) and [A Sentiment Analysis Tool Chain for 18th Century Periodical](https://gitlab.uni.lu/melusina/vdhd/koncar_sentiment).


## An example
![Sentiment Analysis](https://raw.githubusercontent.com/MiMoText/sentiment_novels/main/img/sentiments_voltaire_candide.PNG?raw=true)
Excerpt of chapter two of Voltaire's novel Candide (1759) tagged with sentiments provided by "[A Sentiment Analysis Tool Chain for 18th Century Periodical](https://gitlab.uni.lu/melusina/vdhd/koncar_sentiment)"

## Data 

We utilise the [roman18-corpus](https://github.com/MiMoText/roman18), which contains french novels 1750-1800 in XML/TEI and plain text.  We utilised the novels in modernised plain text.  

## Results

| file |polarity  | subjectivity |
| :------------ |:---------------:| -----:|
|Abbes_Voyage.txt'    | -0.030000690498737378 |0.671139971139971 |
| Anonym_Suzon.txt'   | 0.17621220020855063      |   0.49699339589850516 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |
| zebra stripes | are neat        |    $1 |

## Licence

Software in this repo, unless specified otherwise, is made available under the MIT license. We don’t claim any copyright or other rights on the metadata. If you use our scripts or results, for example in research or teaching, please reference this repository using the citation suggestion below.


## Citation suggestion

Sentiment Analysis on Eighteenth-Century French Novels (1750-1800), edited by Julia Röttgermann and Johanna Konstanciak, MiMoText, Trier Center for Digital Humanities, 2022. URL: https://github.com/MiMoText/sentiment_novels.

