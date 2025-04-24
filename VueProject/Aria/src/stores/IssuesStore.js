import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
// import{} from '@/services/issuesService'
import { useAuthStore } from "./auth";
import router from "@/router";
import { addissuesService,getAllissuesService,getDetailIsSerivce,deleteissuesService,updateIsService,closeOpenIsService, addMessageService,showMessageService,
    deleteMessageService,
    editMessageService,
    getAMyissuesService
} from "@/services/issuesService";

const auth=useAuthStore()
const toast=useToast()

export const useIssuesStore=defineStore({
    id:'issues',

    state: () => ({
    
        singleIssues:{},
        allIssues:[],
        singleMessage:{},
        allMessage:[]
    }),
    actions:{
        
        async addIssues(info,av){
            await addissuesService(auth.user.access,info,av).then((res)=>{
           
                toast.success("پرسش شما با موفقیت ایجاد شد")
                
            }).catch((err)=>{
                console.log(err)
                toast.warning("خطا در ساخت پرسش جدید، لطفا مجددا تلاش فرمایید")
            }).finally((e)=>{
                router.push("/discuss/")
            })
        },

        async getSingleIssues(id,projectID){
            
                await getDetailIsSerivce(auth.user.access,id,projectID).then((res)=>{
                    this.singleIssues=res.data
                }).catch((er)=>{
                    console.log(er)
                })
        },

        async getAllIssues(id){
                await getAllissuesService(auth.user.access,id).then((res)=>{
                
                    this.allIssues=res.data
                }).catch((er)=>{

                    console.log(er)
                })
        },
         async getMyIssues(id,user){
             await getAMyissuesService(auth.user.access,id,user).then((res)=>{
                 
                    this.allIssues=res.data
                }).catch((er)=>{

                    console.log(er)
                })
        },
      async  deleteIssues(id,projectID){
   
        await deleteissuesService(auth.user.access,id,projectID).then((res)=>{
             this.getAllIssues(projectID)
           
             toast.success("پرسش با موفقیت حذف شد.")
        }).catch((er)=>{
                console.log(er)
        })
        },

       async editIssues(info,av,id,projectID){
          await  updateIsService(auth.user.access,info,av,id,projectID).then((res)=>{
                toast.success("پرسش شما با موفقیت ویرایش شد")
                router.push("/discuss/")
            }).catch((er)=>{
                console.log(er)
            })
        },

        async closeOpenIssues(status,id,projectID){
           await closeOpenIsService(this.singleIssues,auth.user.access,status,id,projectID).then((res)=>{
                if(status==1){
                    toast.success("پرسش  با موفقیت باز شد")
                }else{
                    toast.info("پرسش  با موفقیت بسته شد")

                }
               
                router.push("/discuss/")
            }).catch((er)=>{
                console.log(er)
            })
        },

        async addMessage(info,av){
              
               return await addMessageService(auth.user.access,info,av).then((res)=>{
                     this.getSingleIssues(info.id,info.projectID).then((res)=>{
                        toast.info("پاسخ شما با موفقیت ثبت گردید.")
                     })
                }).catch((er)=>{
                    toast.warning("خطا در اضافه کردن..")
                    console.log(er)
                })
        },


       async showMessage(id,projectID,messageID){
        await showMessageService(auth.user.access,id,projectID,messageID).then((res)=>{
            this.singleMessage=res.data
        }).catch((er)=>{
            console.log(er)
        })
        },

       async deleteMessage(projectID,id,messageID){
     
            return await deleteMessageService(auth.user.access,projectID,id,messageID).then((res)=>{
                this.getSingleIssues(id,projectID)
                toast.success("پاسخ شما با  موفقیت حذف شد.")
            }).catch((er)=>{
                console.log(er)
            })
        },

      async  editMessage(id,projectID,messageID,info,av){
            await editMessageService(auth.user.access,id,projectID,messageID,info,av).then((res)=>{
                toast.success("با موفقیت ویرایش شد")
                router.go(-1)
            }).catch((er)=>{
                console.log(er)
            })
        },
       
    }
    
})