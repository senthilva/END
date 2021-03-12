# English to Python code generation  

The objective is to try and generate python code from english.The machine translation model implementing the [Attention is all you need paper](https://arxiv.org/abs/1706.03762) is used. 

## Data prep-processing

*  Split the file into english and python
*  process entire python content as one line (appending) - factors the tabs; new lines
*  Performed cleaning; removed comments within code ; removed outliers
*  Replaced tabs with 4 spaces
*  regex cleaned irregular spaces : 3 -> 4; 7 -> 8; 11 -> 12 

## Python tokenizer

* Built a custom tokenizer using the spacy(en) as base  
* custom rules
  * key words
  * tabs after : and in blocks
  * == , >=, <= to be treated as single token
  * handled [,],(,),{,}   

## Loss

## Model Training

* Training loss; perplexity kept improving so increased the epochs to 30

## Attention Visualization

## Sample Inferences

## Observations/ Learning

* The model is able to learn the python syntax pretty well : tabs; colon ; keywords
* The amount of training data is less ~4k ; so the model struggles to learn context across words
* Model is overfitting : it is able to translate a single word to entire python code Eg presence of "sigmoid" maps to entire python code
* Needs to understand and generate variables names

## References

* [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)
