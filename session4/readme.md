
# Approach  

- For running the forward function in a loop the below changes were done.   
  - Build 2 RNN functions : **as the dimension of input would change from 2nd layer**. 
  
        self.rnn = nn.LSTM(embedding_dim, 
                           hidden_dim, 
                           num_layers=n_layers, # hardcoding to 1
                           bidirectional=bidirectional, 
                           dropout=dropout)
        
        self.rnn2_onwards = nn.LSTM(hidden_dim, # Using the hidden dimension as input from layer 2
                           hidden_dim, 
                           num_layers=n_layers, # hardcoding to 1
                           bidirectional=bidirectional, 
                           dropout=dropout).  
     and loop them in forward function 
     
        #run for embedding 1st layer
        packed_output, (hidden, cell) = self.rnn(packed_embedded)

        LSTM_LAYERS = 2 # already run for first layer
        for layer in range(LSTM_LAYERS):
            
            packed_output, (hidden, cell) = self.rnn2_onwards(packed_output)
     
  
- Reverse the text (only for training data).  
  - use torch.flip in the training function.  
  
      
      for data_item  in range(len(train_data)):
        vars(train_data.examples[data_item]).get('text').reverse()
  
     
   
