def invalidTransactions(self, transactions: List[str]) -> List[str]:  
        """
            1. parse transactions and store in a dictionary with name as key and the entire transaction as value (this is to group all transactions with the same name)
            2. go through the dict and for each name, use sliding window to get all transactions 60 min apart under that name 
            3. go thru all transactions within 60 min window and check if location is different
            4. keep an invalid array with the same size as transactions to mark which one to add to final output
        """
        parsed = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            parsed.append((name, int(time), int(amount), city, i, transaction)) # store index to avoid adding duplicate invalid transactions and store raw transaction to easy to add output
        
        invalid = [False] * len(transactions) # initialize invalid array to false 

        # mark all transactions over $1000 as invalid 
        for i, transaction in enumerate(parsed):
            if transaction[2] > 1000:
                invalid[i] = True

        # build dictionary    
        myDict = {}
        for transaction in parsed:
            name = transaction[0]
            if name not in myDict:
                myDict[name] = [transaction]
            else:
                myDict[name].append(transaction)
        
        for name, trans in myDict.items():
            trans.sort(key = lambda x: x[1]) # sort by time 

            left = 0
            right = 0
            while right < len(trans):
                # find window where transactions in that window are within 60 min
                while trans[right][1] - trans[left][1] > 60:
                    left += 1
                
                # check if its different city
                for j in range(left, right):
                    if trans[right][3] != trans[j][3]:
                        invalid[trans[right][4]] = True
                        invalid[trans[j][4]] = True
                
                right += 1
            
        return [transaction[5] for transaction, flag in zip(parsed, invalid) if flag]