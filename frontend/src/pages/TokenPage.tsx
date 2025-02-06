import {useEffect} from "react";
import {useParams, useNavigate} from "react-router-dom";

export const TokenPage = () => {
    const {token} = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        if (token) {
            localStorage.setItem("activation", token);
            navigate("/register");
        }
    }, [token, navigate]);

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100 text-center">
            <div>
                <h1 className="font-bold mt-4">Copy the token</h1>
                {token && <p className="w-128 break-words bg-gray-200 p-2 mt-4 mx-auto">{token}</p>}
            </div>
        </div>
    );
};
