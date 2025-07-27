import axios from "@/utils/axios";

const getDetailuser=(token)=>{
    
    return axios.get("auth/users/me/",{
        headers: {
            Authorization:`JWT ${token}`
        }
    })
}
const updateProfile=(token,info,email,avatar)=>{


    return axios.put("auth/users/me/",{
        "avatar":avatar,
        "first_name": info.firstname,
        "last_name": info.lastname,
        "phone_number": info.phone_number,
        "about": info.about,
        "email":email,
        "is_active": true,
        
    },   {
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}
const addUser=(token,info,id)=>{

    return axios.post(`workspace/project/${id}/email/`,{
        "to_email":info.email,
        "level": info.level,
        "skill": info.skill,

    },   {
        headers: {
            Authorization: `JWT ${token}`,

        }
    })
}
const ShowUsers=(token,id)=>{
    return axios.get(`workspace/project/${id}/users/`,  {
        headers: {
            Authorization: `JWT ${token}`,

        }
    })
}
const deleteuserService=(token,id,userId)=>{
    return axios.delete(`workspace/project/${id}/users/${userId}`,  {
        headers: {
            Authorization: `JWT ${token}`,

        }
    })
}

const getLevel=(id,token)=>{
    return axios.get(`workspace/project/${id}/get_user_level_skill`,{headers: {
        Authorization: `JWT ${token}`,
    }
    })
}
export {getDetailuser,updateProfile,addUser,ShowUsers,getLevel,deleteuserService}