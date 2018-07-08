
# coding: utf-8

# In[6]:


import numpy as np
size=[784,16,10] #architecture


# In[7]:


class neural(object):
    __init__(self,size):
        self.w1=np.random.randn(size[1],size[0])
        self.w2=np.random.randn(size[2],size[1])
        self.dw2=np.zeroes(size[2],size[1])
        self.dw1=np.zeroes(size[1],size[0])
        self.b1=np.random.randn(size[1],1)
        self.b2=np.random.randn(size[2],1)
        self.db2=np.zeroes(size[2],1)
        self.db1=np.zeroes(size[1],1)
    
    def training(tr_data,tes_data):
        for x,y in tr_data:
            forward_prop(x)
            deltac=back_prop(y)
            self.dw2=self.dw2+deltac[0]
            self.dw1=self.dw1+deltac[1]
            self.db2=self.db2+deltac[2]
            self.db1=self.db1+deltac[3]
        
         for i in range(self.a2):
            for j in range(self.a1):
                self.w2[i][j]=self.w2[i][j] - learning_rate*self.dw2[i][j]/len(tr_data)
                
        for i in range(self.a1):
            for j in range(self.a0):
                self.w1[i][j]=self.w1[i][j] - learning_rate*self.dw1[i][j]/len(tr_data)
                
        for i in range(self.a2):
            self.b2[i]= self.b2[i] - learning_rate * self.db2[i]/len(tr_data)            
           
        for i in range(self.a1):
            self.b1[i]= self.b1[i] - learning_rate * self.db1[i]/len(tr_data)  
            
            #training complete
            #test data accuracy
        
        test_accuracy(tes_data)
        return
    
         
     
    
    def forward_prop(x):
        self.a0=x
        self.z1=(np.dot(a0,self.w1)+b)
        self.a1=sigmoid(self.z1)
        self.z2=(np.dot(a1,self.2)+b)
        self.a2=sigmoid(self.z2)
        return 
            
      
    def back_prop(y):
        dcda2=2(self.a2-y)
        dcdw2=np.zeroes(self.a2,self.a1)
        for i in range(self.a2):
            for j in range(self.a1):
                dcdw2[i][j]=2*(self.a2[i]-y[i])*sigmoid_prime(self.z2[i])*self.a1[j]
                
        dcdb2=np.zeroes(self.a2,1)   
        for i in range(self.a2):
             dcdw2[i]=2*(self.a2[i]-y[i]) *sigmoid_prime(self.z2[i]) *1
        
        dcda1=np.zeroes(self.a1,1)
        for i in range(self.a1):
            for j in range(self.a2):
                dcda1[i]=dcda1[i] + 2*(self.a2[j]-y[j]) * sigmoid_prime(self.z2[j]) * self.w2[j][i]
                
               
        dcdw1=np.zeroes(self.a1,self.a0)
        for i in range(self.a1):
            for j in range(self.a0):
                dcdw1[i][j]=self.dcda1[i]*sigmoid_prime(self.z1[i])*self.a0[j]
               
        dcdb1=np.zeroes(self.a1,1)   
        for i in range(self.a1):
             dcdb1[i]=self.dcda1[i]*sigmoid_prime(self.z1[i])*self.a0[j]
                
        return [dcdw2,dcdw1,dcdb2,dcdb1]    
        
       
    def sigmoid(z):
        """The sigmoid function."""
        return 1.0/(1.0+np.exp(-z))

    def sigmoid_prime(z):
        """Derivative of the sigmoid function."""
        return sigmoid(z)*(1-sigmoid(z))
            
            
     
    def test_accuracy(tes_data):
        correct_pred=0
        for x,y in tes_data:
            forward_prop(x)
            if y==argmax(self.a2):
                correct_pred = correct_pred + 1
                
        print 'accuracy is' , correct_pred*100/len(tes_data)
        return
        


# In[ ]:




