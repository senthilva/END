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

Built a custom loss function using weights within the crossentropy loss function. The idea was to give a higher weightage for top 50 most common vocab which ten to cover the most used operators. In addition, gave highest weightage for keywords and tabs in vocabulary to force it to learn the syntax.

```python
weight_list = []
for idx,word in enumerate(TRG.vocab.itos):


  #default
  weight = 1.0 
  
  # first 50 except
  #0-3  pad, sos, eos, unk
  if 3 < idx <= 50 :
    weight = 2.0 

  # keyword or tab 
  if (keyword.iskeyword(word)) or ('\n' in word) :
    weight = 3.0
  
  weight_list.append(weight)

class_weights = torch.FloatTensor(weight_list).to(device)

criterion = nn.CrossEntropyLoss(weight=class_weights, ignore_index = TRG_PAD_IDX)
```


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
