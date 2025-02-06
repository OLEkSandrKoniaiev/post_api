import {urls} from "../constants/urls";
import {IPost} from "../models/IPost";
import {authApiService, publicApiService} from "./api.service";

type PostPaginated = {
    total_items: number;
    total_pages: number;
    prev: boolean;
    next: boolean;
    data: IPost[];
};

type CreatePostData = {
    text: string;
};

type UpdatePostData = {
    text?: string;
};

const postsService = {
    getPosts: async (): Promise<PostPaginated> => {
        const {data} = await publicApiService.get(urls.posts.list_create);
        return data;
    },

    createPost: async (postData: CreatePostData): Promise<IPost> => {
        const {data} = await authApiService.post(urls.posts.list_create, postData);
        return data;
    },

    getPost: async (id: string): Promise<IPost> => {
        const {data} = await publicApiService.get(urls.posts.retrieve_update_destroy(id));
        return data;
    },

    updatePost: async (id: string, updateData: UpdatePostData): Promise<IPost> => {
        const {data} = await authApiService.patch(urls.posts.retrieve_update_destroy(id), updateData);
        return data;
    },

    destroyPost: async (id: string): Promise<void> => {
        await authApiService.delete(urls.posts.retrieve_update_destroy(id));
    }
};

export {postsService};
