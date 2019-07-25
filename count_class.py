class Counter:
    
    def __init__(self, arr, final_list=None):
        self.arr = arr
        if final_list == None:
            final_list = []
        self.final_list = final_list
    
    def calc(self, select, order=False):
        self.select = select
        self.order = order
        import itertools
        
        if self.order == False:
            combos = []
            for combo in itertools.combinations(self.arr, self.select):
                combos.append(set(combo))
            self.final_list = []
            for combo in combos:
                if combo not in self.final_list:
                    self.final_list.append(combo)
    
        else:
            perms = []
            for perm in itertools.permutations(self.arr, self.select):
                perms.append(perm)
            self.final_list = []
            for perm in perms:
                if perm not in self.final_list:
                    self.final_list.append(perm)

        return len(self.final_list)