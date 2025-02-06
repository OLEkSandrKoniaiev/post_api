const baseURL = import.meta.env.VITE_API_URL;

const auth = '/auth';
const posts = '/posts';
const users = '/users'
const profiles = '/profiles'

const urls = {
    auth: {
        login: auth,
        refresh: auth + '/refresh',
        activate: auth + '/activate',
        socket: auth + '/socket'
    },
    posts: {
        list_create: posts,
        retrieve_update_destroy: (id: string) => {
            return posts + '/' + id
        }
    },
    users: {
        list_create: users,
        list_online: users + '/online',
        destroy: users + '/delete',
        block: (id: string) => {
            return users + `/${id}/block`
        },
        unblock: (id: string) => {
            return users + `/${id}/unblock`
        },
        user_to_admin: (id: string) => {
            return users + `/${id}/to_admin`
        },
        admin_to_user: (id: string) => {
            return users + `/${id}/to_user`
        },
        profiles: {
            list: users + profiles,
            update: users + profiles + '/patch',
            add_photo: (id: string) => {
                return users + profiles + `/${id}/photos`
            }
        }
    }
}

export {
    baseURL,
    urls
}
