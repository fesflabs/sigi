import os

def generate_queries():
    base_path = "frontend/src/features/contracts/dashboard/api"
    os.makedirs(base_path, exist_ok=True)

    # Definição dos fetchers baseados na Spec
    fetchers = {
        "getMetrics.ts": """
import { api } from '@/shared/api';
import { ContractMetrics } from '../types';

export const getMetrics = async (params: Record<string, any>): Promise<ContractMetrics> => {
  const response = await api.get('/dashboard/contracts/metrics', { params });
  return response.data;
};
""",
        "getEvolution.ts": """
import { api } from '@/shared/api';
import { EvolutionData } from '../types';

export const getEvolution = async (): Promise<EvolutionData[]> => {
  const response = await api.get('/dashboard/contracts/evolution');
  return response.data;
};
"""
    }

    for file_name, content in fetchers.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'w') as f:
            f.write(content.strip())
        print(f"[SKILL] Arquivo gerado: {file_path}")

if __name__ == "__main__":
    generate_queries()