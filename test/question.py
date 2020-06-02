class Question:

    def __init__(self,id,title,is_correct):
        self.id = id
        self.title = title
        self.is_correct = is_correct

    def __repr__(self):
        if self.is_correct:
            return self.title+' TAK'
        else:
            return self.title+' NIE'    

