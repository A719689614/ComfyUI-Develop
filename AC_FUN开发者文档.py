# 定义一个类对象
class AC_FUN_Expression:
    # 把方法以装饰器的形式把普通方法改成类方法
    # 以下是一些格式
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            "int":("INT",{
                "min":0,
                "max":9999,
                "default":1,
                "step":1,}),
            "str": ("STRING", {
                    "multiline": True, 
                    "default": 'this is a string by AC_FUN'}),
            "image": ("IMAGE",{"upload":True}),
            "float": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, 
                                "step": 0.01, "display": "number"}),
            "bool": ("BOOLEAN", {"default":False}),
            "list":(['str','str'],),
            "mask": ("MASK",),
            "samples": ("LATENT",),
            "conditioning_to": ("CONDITIONING", ),
            "clip": ("CLIP", ),
            "control_net": ("CONTROL_NET", ),
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},

              }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',"INT","FLOAT","IMAGE","LATENT",)
    # 返回节点命名
    RETURN_NAMES = ('STRING',)
    # 类方法命名必须与下方类方法名一致
    FUNCTION = "AC_FUNCTION" 
    # 节点类目
    CATEGORY = "AC_FUNV2.1" 
    # 类方法传入的属性与上面装饰器类方法保持一致
    # 可以使用多个类方法及函数嵌套,但目前不支持循环输出
    def AC_FUNCTION(self,str,int,image,float,bool,list):
        return (str,int,image,float,bool,list)        


#do some processing on the image, in this example I just invert it   
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
# 用字典的形式把节点名和类名关联起来("simple":AC_FUN)
# 可写可不写,可以放置到__init.py文件导入的时候统一写
NODE_CLASS_MAPPINGS = {
}

# 这部分可写可不写
# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
}

if __name__ == "__main__":
    pass



