import {useEffect, useState} from "react";
import {IPost} from "../../models/IPost.ts";
import PostComponent from "./PostComponent.tsx";
import {postsService} from "../../services/posts.service.ts";

const PostsComponent = () => {
    const [posts, setPosts] = useState<IPost[]>([]);

    useEffect(() => {
        postsService.getPosts().then((response) => {
            if ("detail" in response) {
                console.error(response);
            } else {
                setPosts(response.data);
            }
        });
    }, []);

    return (
        <div className="container">
            <div className="grid-container">
                {posts.map((post) => (
                    <PostComponent key={post.id} item={post}/>
                ))}
            </div>
        </div>
    );
};

export default PostsComponent;
