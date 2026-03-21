from supabase import create_client

class GameManager:
    def __init__(self, url: str, key: str):
        self.supabase = create_client(url, key)

    def new_game_nr(self):
        response = self.supabase.table("games").select("*").execute()
        game_data = response.data
        return len(game_data) + 1

    def new_game(self, game_nr, date):
        response = self.supabase.table("games").insert({
            "game_nr": game_nr,
            "game_date": date,
        }).execute()

        if not response.data:
            return None

        return response.data[0]

    def new_game_player_data(self, game_id, player_id, final_rank, vite_donate, vite_ricevute):
        response = self.supabase.table("game_results").insert({
            "game_id": game_id,
            "player_id": player_id,
            "final_rank": final_rank,
            "lives_donated_total": vite_donate,
            "lives_received_total": vite_ricevute,
        }).execute()

        if not response.data:
            return None

        return response.data[0]

    def new_note(self, game_nr, note):
        response = self.supabase.table("game_notes").insert({
            "game_id": game_nr,
            "note_text": note,
        }).execute()

        if not response.data:
            return None

        return response.data[0]

    def games_played(self):
        response = self.supabase.table("games").select("*").execute()
        game_data = response.data
        return game_data

    def get_game_data(self, game_id):
        response = self.supabase.table("game_results").select("*").eq("game_id", game_id).execute()
        game_data = response.data
        return game_data