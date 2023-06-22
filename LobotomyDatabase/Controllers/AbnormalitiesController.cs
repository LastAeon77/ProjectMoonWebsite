using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using LobotomyDatabase.Data;
using LobotomyDatabase.Models;
using System.Collections.ObjectModel;
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.CompilerServices;

namespace LobotomyDatabase.Controllers
{
	[Route("asp/api/[controller]")]
	[ApiController]
	public class AbnormalitiesController : ControllerBase
	{
		private readonly LobotomyData _context;

		public AbnormalitiesController(LobotomyData context)
		{
			_context = context;
		}

		public class AbnormailityStoryDto
		{
			public string? Story { get; set; }
			public string? StoryNumb { get; set; }
		}
		public class AbnormailityTipDto
		{
			public string? Tip { get; set; }
			public string? TipNum { get; set; }
		}
		public class AbnormailityNarrationDto
		{
			public string? Narration { get; set; }
			public string? NarrationAction { get; set; }
		}

		public class AbnormailityDto
		{
			public int ID { get; set; }
			public string? in_game_id { get; set; }
			public string? Name { get; set; }
			public string? NumCode { get; set; }
			public string? RiskLevel { get; set; }
			public string? OpenText { get; set; }
			public IEnumerable<AbnormailityStoryDto>? Stories { get; set; }
			public IEnumerable<AbnormailityTipDto>? Tips { get; set; }
			public IEnumerable<AbnormailityNarrationDto>? Narrations { get; set; }
		}


		// GET: api/Abnormalities
		[HttpGet]
		public async Task<ActionResult<List<AbnormailityDto>>> GetAbnormalities()
		{


			var abnos = await _context.Abnormalities
				.Select(x => new AbnormailityDto()
				{
					ID = x.ID,
					in_game_id = x.in_game_id,
					Name = x.Name,
					NumCode = x.NumCode,
					RiskLevel = Enum.GetName<RiskLevel>((RiskLevel)x.RiskLevel),
					OpenText = x.OpenText,
					Stories = x.Stories.Select(y => new AbnormailityStoryDto()
					{
						Story = y.Story,
						StoryNumb = y.StoryNumb
					}),
					Tips = x.Tips.Select(y=>new AbnormailityTipDto()
					{
						Tip = y.Tip,
						TipNum = y.TipNum

					}),
					Narrations = x.Narrations.Select(y => new AbnormailityNarrationDto()
					{
						Narration = y.Narration,
						NarrationAction = y.NarrationAction

					}),
				}).ToListAsync();
			return abnos;
		}

		// GET: api/Abnormalities/5
		[HttpGet("{id}")]
		public async Task<ActionResult<Abnormality>> GetAbnormality(int id)
		{
			if (_context.Abnormalities == null)
			{
				return NotFound();
			}
			var abnormality = await _context.Abnormalities.FindAsync(id);

			if (abnormality == null)
			{
				return NotFound();
			}

			return abnormality;
		}

		// PUT: api/Abnormalities/5
		// To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
		[HttpPut("{id}")]
		public async Task<IActionResult> PutAbnormality(int id, Abnormality abnormality)
		{
			if (id != abnormality.ID)
			{
				return BadRequest();
			}

			_context.Entry(abnormality).State = EntityState.Modified;

			try
			{
				await _context.SaveChangesAsync();
			}
			catch (DbUpdateConcurrencyException)
			{
				if (!AbnormalityExists(id))
				{
					return NotFound();
				}
				else
				{
					throw;
				}
			}

			return NoContent();
		}

		// POST: api/Abnormalities
		// To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
		[HttpPost]
		public async Task<ActionResult<AbnormailityDto>> PostAbnormality([FromBody] AbnormailityDto abnormality)
		{
			if (_context.Abnormalities == null)
			{
				return Problem("Entity set 'LobotomyData.Abnormalities'  is null.");
			}
			Abnormality ab = new Abnormality();
			ab.Name = abnormality.Name;
			ab.in_game_id = abnormality.in_game_id;
			ab.NumCode = abnormality.NumCode;
			ab.RiskLevel = Enum.Parse<RiskLevel>(abnormality.RiskLevel,true);
			ab.Stories = new Collection<AbnormalityStory>();
			ab.Tips = new Collection<AbnormalityTip>();
			ab.Narrations = new Collection<AbnormalityNarration>();
			ab.OpenText = abnormality.OpenText;
			foreach (AbnormailityStoryDto story in abnormality.Stories)
			{
				AbnormalityStory new_story = new AbnormalityStory();
				new_story.Story = story.Story;
				new_story.StoryNumb = story.StoryNumb;
				/*_context.AbnormalitiesStories.Add(new_story);*/
				ab.Stories.Add(new_story);
			}
			foreach (AbnormailityTipDto tip in abnormality.Tips)
			{
				AbnormalityTip new_tip = new AbnormalityTip();
				new_tip.Tip = tip.Tip;
				new_tip.TipNum = tip.TipNum;
				/*_context.AbnormalitiesTips.Add(new_tip);*/
				ab.Tips.Add(new_tip);
			}

			foreach (AbnormailityNarrationDto narration in abnormality.Narrations)
			{
				AbnormalityNarration new_narration = new AbnormalityNarration();
				new_narration.Narration = narration.Narration;
				new_narration.NarrationAction = narration.NarrationAction;
				/*_context.AbnormalitiesTips.Add(new_tip);*/
				ab.Narrations.Add(new_narration);
			}
			_context.Abnormalities.Add(ab);
			await _context.SaveChangesAsync();
			
			return abnormality;
		}

		// DELETE: api/Abnormalities/5
		[HttpDelete("{id}")]
		public async Task<IActionResult> DeleteAbnormality(int id)
		{
			Abnormality to_be_deleted = _context.Abnormalities.Include(q => q.Stories).Include(q => q.Narrations).Include(q => q.Tips).Where(s => s.ID == id).FirstOrDefault();
			if (to_be_deleted == null)
			{
				return Content("Bad Request");
			}
			_context.Abnormalities.Remove(to_be_deleted);
			await _context.SaveChangesAsync();

			return NoContent();
		}

		private bool AbnormalityExists(int id)
		{
			return (_context.Abnormalities?.Any(e => e.ID == id)).GetValueOrDefault();
		}
	}
}
