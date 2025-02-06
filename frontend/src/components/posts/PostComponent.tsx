import {FC} from "react";
import {IPost} from "../../models/IPost.ts";

type PostPropType = {
    item: IPost;
};

const PostComponent: FC<PostPropType> = ({item}) => {
    return (
        <div className="card">
            <p className="text-base text-gray-800">{item.text}</p>
        </div>
    );
};

export default PostComponent;
