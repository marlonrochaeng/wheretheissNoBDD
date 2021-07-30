class Utils():

    @staticmethod
    def convert_list_to_string(information):
        information_list_to_str = ''
        for i in information:
            if i != information[-1]:
                information_list_to_str += str(i) + ','
            else:
                information_list_to_str += str(i)
        return information_list_to_str
