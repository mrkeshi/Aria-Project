import { defineStore } from "pinia";
import { login, verify,refresh, active } from "@/services/auth";
import { useToast } from "vue-toastification";
import router from "@/router";

const toast=useToast()
export const useAuthStore=defineStore({
    id:'auth',
    state: () => ({
        user: {
            access: null,
            refresh: null,
            email: null,
        },
        returnUrl: null,

    }),

    actions:{

        async active(email){
            active(email).then((ax)=>{
                toast.success("ایمیل فعالسازی مجدد برای شما ارسال شد")
            })
        },
        async loginActions (username,password){
            await login(username,password).then((response)=>{
                this.user.email=username
                this.user.access=response.data.access
                this.user.refresh=response.data.refresh
                
                toast.success("باموفقیت لاگین شد")
                localStorage.setItem('user',JSON.stringify(this.user))
                router.push(this.returnUrl || '/dashboard');
                
            }).catch((error)=>{
                let msg=error.response.data.detail  
       
                if(msg.includes("active")){
                    toast.error("لطفا صندوق ورودی ایمیل را چک کنید و اقدام به فعالسازی حساب نمایید")
                }else{
                    toast.error(msg)
                }
              
            })
        },
       async logoutAction() {
            this.user = {
                access: null,
                refresh: null,
                email: null,
            };
            localStorage.removeItem('user');
            
            toast.warning("شما خارج شدید")
            router.push('/login');
        },
        async verifyAction(url){
     
            this.returnUrl=url
         
            let userlocal = localStorage.getItem('user');
            userlocal = JSON.parse(userlocal);
           
            if(userlocal){
            await verify(userlocal.access).then((response)=>{
                this.user.access=userlocal.access
               console.log("SETTTTTT TOOKEN JWT")

                this.user.refresh=userlocal.refresh
                this.user.email=userlocal.email
            }).catch((er)=>{
                router.push('/login');
                toast.error("توکن شما منقضی شده است، لطفا دوباره وارد شوید")
            
            })
        }else{
            router.push('/login');
            toast.error("اجازه دسترسی به این صفحه را ندارید لطفا وارد شوید.")
        }
    }
    }
})