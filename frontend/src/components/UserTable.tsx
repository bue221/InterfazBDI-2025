import { useState, useEffect } from 'react';
import axios from 'axios';

interface User {
    CONSECUSER: number;
    NOMBRE: string;
    APELLIDO: string;
    USUARIO: string;
    FECHAREGISTRO: string;
    EMAIL: string;
    CELULAR: string;
    CODUBICA: string;
}

export function UserTable() {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:3001/usuarios');
            setUsers(response.data);
            setError(null);
        } catch (err) {
            setError('Error al cargar los usuarios');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (consecUser: number) => {
        if (!confirm('¿Estás seguro de que deseas eliminar este usuario?')) return;

        try {
            await axios.delete(`http://localhost:3001/usuarios/${consecUser}`);
            setUsers(users.filter(user => user.CONSECUSER !== consecUser));
        } catch (err) {
            setError('Error al eliminar el usuario');
            console.error(err);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    if (loading) return <div className="text-center p-4">Cargando...</div>;
    if (error) return <div className="text-red-500 text-center p-4">{error}</div>;

    return (
        <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                    <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Apellido</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Usuario</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Celular</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {users.map((user) => (
                        <tr key={user.CONSECUSER}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.CONSECUSER}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.NOMBRE}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.APELLIDO}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.USUARIO}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.EMAIL}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{user.CELULAR}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                <button
                                    onClick={() => handleDelete(user.CONSECUSER)}
                                    className="text-red-600 hover:text-red-900"
                                >
                                    Eliminar
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
} 