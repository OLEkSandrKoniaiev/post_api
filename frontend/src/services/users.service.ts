import {IUser} from "../models/IUser";
import {urls} from "../constants/urls";
import {authApiService, publicApiService} from "./api.service";
import {IProfile} from "../models/IProfile";

type UserPaginated = {
    total_items: number;
    total_pages: number;
    prev: boolean;
    next: boolean;
    data: IUser[];
};

type ProfilePaginated = {
    total_items: number;
    total_pages: number;
    prev: boolean;
    next: boolean;
    data: IProfile[];
};

type CreateUserData = {
    email: string;
    password: string;
    profile: {
        name: string;
        surname: string;
        age: number;
    };
};

type UpdateProfileData = {
    name?: string;
    surname?: string;
    age?: number;
};

const userService = {
    getUsers: async (): Promise<UserPaginated> => {
        const {data} = await authApiService.get(urls.users.list_create);
        return data;
    },

    createUser: async (postData: CreateUserData): Promise<IUser> => {
        const {data} = await authApiService.post(urls.users.list_create, postData);
        return data;
    },

    getOnlineUsers: async (): Promise<UserPaginated> => {
        const {data} = await authApiService.get(urls.users.list_online);
        return data;
    },

    destroyUser: async (): Promise<void> => {
        await authApiService.delete(urls.users.destroy);
    },

    blockUser: async (id: string): Promise<IUser> => {
        const {data} = await authApiService.patch(urls.users.block(id));
        return data;
    },

    unblockUser: async (id: string): Promise<IUser> => {
        const {data} = await authApiService.patch(urls.users.unblock(id));
        return data;
    },

    userToAdmin: async (id: string): Promise<IUser> => {
        const {data} = await authApiService.patch(urls.users.user_to_admin(id));
        return data;
    },

    adminToUser: async (id: string): Promise<IUser> => {
        const {data} = await authApiService.patch(urls.users.admin_to_user(id));
        return data;
    },

    getProfiles: async (): Promise<ProfilePaginated> => {
        const {data} = await publicApiService.get(urls.users.profiles.list);
        return data;
    },

    updateProfile: async (updateData: UpdateProfileData): Promise<IProfile> => {
        const {data} = await authApiService.patch(urls.users.profiles.update, updateData);
        return data;
    },

    addProfilePhoto: async (id: string, file: File): Promise<{ photo: string }> => {
        const formData = new FormData();
        formData.append("photo", file);

        const {data} = await authApiService.patch(urls.users.profiles.add_photo(id), formData, {
            headers: {"Content-Type": "multipart/form-data"}
        });
        return data;
    }
};

export {userService};
