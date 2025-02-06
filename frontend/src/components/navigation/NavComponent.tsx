import {Link} from "react-router-dom";
import icon from '../../assets/some_icon.jpg';

export const NavComponent = () => {
    return (
        <div className="bg-gray-800 p-2.5 rounded-md w-full shadow-md">
            <ul className="list-none m-0 p-0 flex justify-center">
                <li className="mx-4">
                    {/*молодша сестра хотіла допомогти малюнком :D*/}
                    <img src={icon} alt="icon" className="w-8 h-8"/>
                </li>
                <li className="mx-4">
                    <Link
                        to="login"
                        className="text-gray-300 text-base font-bold transition duration-300 ease-in-out hover:text-blue-400 hover:scale-110"
                    >
                        Login
                    </Link>
                </li>
                <li className="mx-4">
                    <Link
                        to="register"
                        className="text-gray-300 text-base font-bold transition duration-300 ease-in-out hover:text-blue-400 hover:scale-110"
                    >
                        Register
                    </Link>
                </li>
                <li className="mx-4">
                    <Link
                        to="posts"
                        className="text-gray-300 text-base font-bold transition duration-300 ease-in-out hover:text-blue-400 hover:scale-110"
                    >
                        Home
                    </Link>
                </li>
                <li className="mx-4">
                    <Link
                        to="users"
                        className="text-gray-300 text-base font-bold transition duration-300 ease-in-out hover:text-blue-400 hover:scale-110"
                    >
                        Users
                    </Link>
                </li>
            </ul>
        </div>
    );
};
