class Solution:
    def countSeniors(self, details: List[str]) -> int:
        gp_gm_count=0
        for person in details:
            age_string=person[11:13]
            age=int(age_string)
            if age>60:
                gp_gm_count+=1
        return gp_gm_count