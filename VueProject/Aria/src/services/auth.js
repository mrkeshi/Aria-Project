import axios from "@/utils/axios";

const register=(user)=>{
    return axios.post("auth/users/",{
       
        "email": user.email,
        "password": user.password,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number":user.phone_number,
        "re_password": user.confirmpassword
    })
}

const login=(username,password)=>{
    return axios.post("auth/jwt/create",{
            "email":username,
            "password":password
    })
}  
const  verify=async(token)=>{
return await axios.post(`auth/jwt/verify/`,{
    "token":token
})
}
const refresh=(token)=>{
    return axios.post(`auth/jwt/refresh/`,{
        "refresh":token
    })
    }
const active=(email)=>{
    return axios.post('auth/users/resend_activation/',{
        'email':email
    })
}

const forgotpass=(email)=>{
    console.log(email)
    return axios.post("auth/users/reset_password/",{
        "email":email
    })
}
const reset_password=(uid,token,password)=>{
    return axios.post("auth/users/reset_password_confirm/",{
        "uid":uid,
        "token":token,
        "new_password":password
    })
}

export {register,login,verify,refresh,forgotpass,reset_password,active}